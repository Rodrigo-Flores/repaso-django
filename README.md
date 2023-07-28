# Comandos básicos de terminal para Django
A continuación, se presentan algunos comandos básicos de terminal que son útiles para trabajar con Django, un framework web de Python. Estos comandos te ayudarán a crear proyectos, aplicaciones y ejecutar el servidor de desarrollo.

## Crear un nuevo proyecto y aplicación:
Crear un nuevo proyecto de Django:
```sh
django-admin startproject core .
```
> _Nota: El punto al final indica que el proyecto se creará en el directorio actual._

Crear una nueva aplicación dentro del proyecto:
```sh
python manage.py startapp nombre_app
```

## Administrar la base de datos:
Crear las tablas en la base de datos (sincronizar modelos):
```sh
python manage.py migrate
```

Crear una migración para los cambios realizados en los modelos:
```sh
python manage.py makemigrations
```

Aplicar migraciones pendientes:
```sh
python manage.py migrate
```

Crear un superusuario (administrador) para el proyecto:
```sh
python manage.py createsuperuser
```

## Ejecutar el servidor de desarrollo

Iniciar el servidor de desarrollo:
```sh
python manage.py runserver
```
