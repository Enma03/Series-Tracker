Flask Anime Series App
Esta aplicación web permite a los usuarios ver y seguir series de anime. La aplicación está construida con Flask y utiliza Supabase como backend para la base de datos.

Características
Registro e inicio de sesión de usuarios.
Visualización de series de anime disponibles.
Posibilidad de seguir y dejar de seguir series.
Almacena las series seguidas por cada usuario.
1.Clona el repositorio:
git clone https://github.com/tuusuario/flask-anime-series-app.git
cd flask-anime-series-app
2.Crea un entorno virtual:
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
3.Instala las dependencias:
pip install -r requirements.txt
4.Crea un archivo .env en el directorio raíz del proyecto y añade tus credenciales de Supabase y una clave secreta:
SUPABASE_URL=tu_supabase_url
SUPABASE_KEY=tu_supabase_key
SECRET_KEY=tu_secret_key
5.Ejecuta la aplicación:
python app.py
La aplicación debería estar disponible en http://127.0.0.1:5000.

Uso
Registro
Accede a http://127.0.0.1:5000/register.
Ingresa un nombre de usuario y una contraseña para registrarte.
Inicio de Sesión
Accede a http://127.0.0.1:5000/auth.
Ingresa tu nombre de usuario y contraseña para iniciar sesión.
Visualización de Series
Desde la página principal, puedes ver todas las series disponibles.
Haz clic en una serie para ver más detalles.
Seguir y Dejar de Seguir Series
Mientras visualizas los detalles de una serie, puedes seguirla haciendo clic en "Seguir".
Para dejar de seguir una serie, haz clic en "No Seguir".
Estructura del Proyecto
app.py: Contiene la lógica principal de la aplicación.
templates/: Directorio que contiene las plantillas HTML.
static/: Directorio para archivos estáticos como CSS e imágenes.
Rutas Principales
/: Página principal que muestra las series disponibles.
/register: Página de registro de usuarios.
/auth: Página de inicio de sesión.
/logout: Cierra la sesión del usuario.
/series/<int:series_id>: Muestra los detalles de una serie específica.
/follow_series: Permite a los usuarios seguir una serie (requiere inicio de sesión).
/unfollow_series: Permite a los usuarios dejar de seguir una serie (requiere inicio de sesión).
Base de Datos
La aplicación utiliza Supabase como backend para la base de datos. Las tablas principales son:

db_users: Almacena la información de los usuarios.
db_series: Almacena la información de las series.
users_series: Almacena la relación entre usuarios y series seguidas.