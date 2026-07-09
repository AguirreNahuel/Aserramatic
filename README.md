# Aserramatic

Sistema de gestión para aserraderos desarrollado con Django.

## Funcionalidades

* Gestión de usuarios.
* Administración de inventario.
* Configuración centralizada del sistema.
* Panel administrativo de Django.
* Gestión de productos y stock.

## Tecnologías

* Python
* Django 6
* PostgreSQL / SQLite
* django-environ
* WhiteNoise
* Gunicorn

## Requisitos

Antes de comenzar, asegurate de tener instalado:

* Python 3.10 o superior
* pip

Para verificar que Python está instalado correctamente, abrí una terminal y ejecutá:

```bash
python --version
```

## Instalación

Todos los comandos de esta sección deben ejecutarse desde una terminal (Símbolo del sistema, PowerShell o Terminal).

### Clonar el repositorio

Ejecutá:

```bash
git clone https://github.com/AguirreNahuel/Aserramatic.git
```

Este comando descargará el proyecto en una carpeta llamada `Aserramatic`.

Luego ingresá a la carpeta del proyecto:

```bash
cd Aserramatic
```

Si cambiaste el nombre de la carpeta o clonaste el repositorio en una carpeta con otro nombre, utilizá ese nombre en lugar de `Aserramatic`.

A partir de este punto, todos los comandos deben ejecutarse dentro de la carpeta del proyecto.

### Crear entorno virtual

Con la terminal ubicada dentro de la carpeta del proyecto, ejecutá:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` que contendrá el entorno virtual.

### Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Si la activación fue correcta, la terminal mostrará algo similar a:

```text
(venv) C:\ruta\al\proyecto>
```

### Instalar dependencias

Con el entorno virtual activado, ejecutá:

```bash
pip install -r requirements.txt
```

## Configuración

Antes de ejecutar el proyecto es necesario crear un archivo `.env` en la raíz del proyecto.

La raíz del proyecto es la misma carpeta donde se encuentra el archivo `manage.py`.

### Generar una SECRET_KEY

Con la terminal ubicada en la carpeta del proyecto, ejecutá:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

El comando devolverá una clave similar a:

```text
django-insecure-4l1#9v7!t4s2...
```

### Crear el archivo .env

En la misma carpeta donde se encuentra `manage.py`, creá un archivo llamado `.env` con el siguiente contenido:

```env
# Clave generada en el paso anterior
SECRET_KEY=django-insecure-4l1#9v7!t4s2...
DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=sqlite:///db.sqlite3
```

Reemplazá el valor de `SECRET_KEY` por la clave generada en el paso anterior.

### Variables de entorno

| Variable      | Descripción                           |
| ------------- | ------------------------------------- |
| SECRET_KEY    | Clave secreta utilizada por Django    |
| DEBUG         | Modo desarrollo (`True` o `False`)    |
| ALLOWED_HOSTS | Hosts permitidos separados por comas  |
| DATABASE_URL  | Cadena de conexión a la base de datos |

## Migraciones

Con la terminal ubicada en la carpeta del proyecto y el entorno virtual activado, ejecutá:

```bash
python manage.py migrate
```

Este comando creará las tablas necesarias en la base de datos.

## Crear usuario administrador

Con la terminal ubicada en la carpeta del proyecto y el entorno virtual activado, ejecutá:

```bash
python manage.py createsuperuser
```

Luego seguí los pasos que aparecen en la terminal:

* Ingresar un nombre de usuario.
* Ingresar una dirección de correo electrónico (opcional).
* Ingresar una contraseña.
* Confirmar la contraseña.

Si la contraseña ingresada es considerada débil, Django mostrará una advertencia y preguntará si se desea continuar. En ese caso, escribí `y` y presioná Enter para crear el usuario igualmente.

## Ejecutar el proyecto

Con la terminal ubicada en la carpeta del proyecto y el entorno virtual activado, ejecutá:

```bash
python manage.py runserver
```

Si el servidor inicia correctamente, aparecerá un mensaje indicando que Django está ejecutándose.

Abrí tu navegador y accedé a:

```text
http://127.0.0.1:8000/
```

Para acceder al panel de administración:

```text
http://127.0.0.1:8000/admin/
```

Utilizá el usuario administrador creado en el paso anterior.

## Dependencias principales

* Django 6.0.5
* django-environ
* python-dotenv
* dj-database-url
* psycopg2-binary
* WhiteNoise
* Gunicorn
* tzdata

## Producción

Configuración habitual para despliegues:

* `DEBUG=False`
* Configuración de `ALLOWED_HOSTS`
* Base de datos PostgreSQL
* Ejecución mediante Gunicorn

## Licencia

Proyecto desarrollado por Nahuel Aguirre.
