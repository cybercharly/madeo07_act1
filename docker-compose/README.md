# Proyecto con Docker Compose - Aplicación Python y Base de Datos SQLite

## Descripción de la Actividad

El proyecto consiste en crear una aplicación web utilizando **Python** y **Docker**. La aplicación se ejecutará dentro de un contenedor y mostrará los datos de una persona registrada en una base de datos SQLite, que se almacenará en otro contenedor.

La base de datos SQLite será creada automáticamente y poblada con un registro de ejemplo de una persona (nombre y correo) al inicializar los contenedores.

Ambos contenedores estarán basados en **Amazon Linux 2023** y se coordinarán utilizando **Docker Compose**.

---

## Modo de Uso

### Pre-requisitos
* Tener **Docker** y **Docker Compose** instalados en tu sistema.
* Opcional: Un entorno **Linux** o **Mac** es recomendado para una experiencia más fluida, pero también puede ejecutarse en **Windows** con Docker Desktop.

---

## Comenzando la Actividad

***Ejemplo***

### Paso 1: Clona este repositorio en tu máquina local:
```bash
git clone git@github.com:cybercharly/madeo07_act1.git
cd docker-compose
```
### Paso 2: Construir y ejecutar los contenedores
```bash
docker-compose up --build
```

### Paso 3: Acceder a la Aplicación
Abre tu navegador y navega a http://localhost:5000. Deberías ver un mensaje similar al siguiente:
```bash
<h1>Hola, Juan Carlos!</h1>
<p>Email: jc.przhdz@gmail.com</p>
```

**Salidas de Pantalla**
| Nombre | Descripcion |
|------|-------------|
| HTTP Status | Código de estado 200 para respuestas exitosas |
| Contenido | Mensaje "Hola Mundo" en formato HTML |
| Puerto | La aplicación escucha en el puerto 5000 |
| Logs | Mensaje en la terminal confirmando el servidor en ejecución |


### Notable
* Este ejemplo está optimizado para ser ejecutado en cualquier sistema operativo que soporte Docker, eliminando la necesidad de configuraciones complejas.
* Si estás en Windows, asegúrate de tener Docker Desktop instalado y en funcionamiento.

## Actividad Realizada Por
| Nombre | Email |
|------|-------|
| Juan Carlos Perez Hernandez | jc.przhdz@gmail.com |

# CHANGELOG
***
### Version 1.0.0
***Added***
* Se agregó el archivo docker-compose.yml para coordinar los contenedores.
* Se agregó el Dockerfile para crear la aplicación en Python.
* Se agregó el archivo app.py para la lógica de la aplicación.
* Se configuró la base de datos SQLite para almacenar los datos de una persona.
* Se creó el README.md con las instrucciones para ejecutar el proyecto.