# Series Trakers

Esta aplicación web permite a los usuarios ver y seguir series de anime. La aplicación está construida con Flask y utiliza Supabase como backend para la base de datos.

### Características

* Registro e inicio de sesión de usuarios.
* Visualización de series de anime disponibles.
* Posibilidad de seguir y dejar de seguir series.
* Almacena las series seguidas por cada usuario.

## Instalación

1. **Clona el repositorio:**

```bash
git clone https://github.com/tuusuario/flask-anime-series-app.git
cd flask-anime-series-app
```

2. **Crear un entorno virtual:**

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows usa .venv\Scripts\activate
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Crea un archivo .env en el directorio raíz del proyecto y añade tus credenciales de Supabase y una clave secreta:**

```
SUPABASE_URL=tu_supabase_url
SUPABASE_KEY=tu_supabase_key
SECRET_KEY=tu_secret_key
```

5. **Ejecuta la aplicación:**

```bash
python app.py
```

La aplicación debería estar disponible en http://127.0.0.1:5000.

## Uso

**Registro**

* Accede a http://127.0.0.1:5000/register.

Ingresa un nombre de usuario y una contraseña para registrart**e.**

**Inicio de Sesión**

* Accede a http://127.0.0.1:5000/auth.

Ingresa tu nombre de usuario y contraseña para iniciar sesión.

**Visualización de Series**

1. Desde la página principal, puedes ver todas las series disponibles.
2. Haz clic en una serie para ver más detalles.
3. Seguir y Dejar de Seguir Series
4. Mientras visualizas los detalles de una serie, puedes seguirla haciendo clic en "Seguir".
5. Para dejar de seguir una serie, haz clic en "No Seguir".

## Estructura del Proyecto

* [app.py](https://github.com/Enma03/Series-Tracker/blob/main/app.py): Contiene la lógica principal de la aplicación.
* [templates/](https://github.com/Enma03/Series-Tracker/tree/main/templates): Directorio que contiene las plantillas HTML.
* [static/](https://github.com/Enma03/Series-Tracker/tree/main/static): Directorio para archivos estáticos como CSS e imágenes.

### Rutas Principales

* /: Página principal que muestra las series disponibles.
* /register: Página de registro de usuarios.
* /auth: Página de inicio de sesión.
* /logout: Cierra la sesión del usuario.
* /series/[int:series_id](int:series_id): Muestra los detalles de una serie específica.
* /follow_series: Permite a los usuarios seguir una serie (requiere inicio de sesión).
* /unfollow_series: Permite a los usuarios dejar de seguir una serie (requiere inicio de sesión).

### Base de Datos

La aplicación utiliza Supabase como backend para la base de datos. Las tablas principales son:

* db_users: Almacena la información de los usuarios.
* db_series: Almacena la información de las series.
* users_series: Almacena la relación entre usuarios y series seguidas.

## Screenshots

**Página de inicio:**

![1722524281977](image/README/1722524281977.png)

**Pagina de inicio, luego de iniciar sección:**

![1722524351723](image/README/1722524351723.png)

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](https://github.com/Enma03/Series-Tracker/blob/main/LICENSE) para más detalles.

## Agradecimientos

Gracias por la ayuda a [LePravda Group](https://github.com/lepravdag).
