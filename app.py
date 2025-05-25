from flask import (Flask, redirect, render_template, request,
                   flash, session, url_for)

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_user_series(user_id):
    response = supabase.table('users_series').select('series_id').eq('user_id', user_id).single().execute()
    series_ids = response.data.get('series_id', []) if response.data else []
    followed_series = []
    for series_id in series_ids:
        series_response = supabase.table('db_series').select('*').eq('series_id', series_id).single().execute()
        if series_response.data:
            followed_series.append(series_response.data)
    return followed_series

@app.route('/')
def index():
    response = supabase.table('db_series').select('*').execute()
    if response.data:
        series_data = response.data
        followed_series = []
        if 'user_id' in session:
            followed_series = get_user_series(session['user_id'])
        return render_template('index.html', series=series_data, followed_series=followed_series)
    flash('No hay series disponibles.', 'info')
    return render_template('index.html', series=[], followed_series=[])

@app.route('/series/<int:series_id>')
def serie(series_id):
    response = supabase.table('db_series').select('*').eq('series_id', series_id).execute()
    serie_info = response.data[0] if response.data else None
    if serie_info is None:
        return "Serie no encontrada", 404
    return render_template('serie.html', serie=serie_info)

@app.route('/follow_series', methods=['POST'])
def follow_series():
    new_series_id = request.form['series_id']
    if 'user_id' in session:
        user_id = session['user_id']
        response = supabase.table('users_series').select('series_id').eq('user_id', user_id).single().execute()  
        if response.data:
            series_ids = response.data.get('series_id', [])
            if new_series_id in series_ids:
                flash('La serie ya está en tu lista.', 'info')
            else:
                series_ids.append(new_series_id)
                supabase.table('users_series').update({'series_id': series_ids}).eq('user_id', user_id).execute()
                flash('Serie agregada con éxito!', 'success')
        else:
            supabase.table('users_series').insert({'user_id': user_id, 'series_id': [new_series_id]}).execute()
            flash('Serie agregada con éxito!', 'success')
        return redirect(url_for('serie', series_id=new_series_id))

    flash('Debes estar logueado para seguir una serie.', 'warning')
    return redirect(url_for('serie', series_id=new_series_id))
            
@app.route('/unfollow_series', methods=['POST'])
def unfollow_series():
    serie_id = request.form['series_id']
    if 'user_id' in session:
        user_id = session['user_id']
        response = supabase.table('users_series').select('series_id').eq('user_id', user_id).single().execute()  
        if response.data:
            series_ids = response.data.get('series_id', [])
            if serie_id not in series_ids:
                flash('La serie no está en tu lista.', 'info')
            else:
                series_ids.remove(str(serie_id))
                supabase.table('users_series').update({'series_id': series_ids}).eq('user_id', user_id).execute()
                flash('Serie eliminada con éxito!', 'success')
        return redirect(url_for('serie', series_id=serie_id))
    flash('Debes estar logueado para dejar de seguir una serie.', 'warning')
    return redirect(url_for('serie',  series_id=serie_id))

class User(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        
@login_manager.user_loader
def load_user(user_id):
    response = supabase.table("db_users").select("*").eq("user_id", user_id).execute()
    if response.data:
        user_data = response.data[0]
        return User(user_data['user_id'], user_data['username'], user_data['password'])
    return None

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        response = supabase.table("db_users").select("user_id").eq("username", username).execute()
        if response.data:
            flash('El nombre de usuario ya existe.')
        else:
            response = supabase.table('db_users').insert({'username': username, 'password': generate_password_hash(password)}).execute()
            user_id = response.data[0]['user_id']
            response = supabase.table('users_series').insert({'user_id': user_id}).execute()
            session['user_id'] = user_id
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/auth', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        response = supabase.table("db_users").select("user_id, username, password").eq("username", username).execute()
        if response.data:
            user_data = response.data[0]
            password_hash = user_data['password']
            if check_password_hash(password_hash, password):
                user = User(user_data['user_id'], user_data['username'], password_hash)
                login_user(user)
                print(f"Inicio de sesión exitoso para el usuario: {username}")
                session['user_id'] = user_data['user_id']
                return redirect(url_for('index'))
        print(f"Intento de inicio de sesión fallido para el usuario: {username}")
        flash('Nombre de usuario o contraseña incorrectos.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(port=3000, debug=True)
