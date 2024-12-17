# CONTENEDORES

## Descripción de la Actividad - nodejs_app_docker

El proyecto consiste en crear una aplicación web simple utilizando **Node.js** y **Docker**. La aplicación desplegará un servidor web básico que publica un mensaje de "Hola Mundo" en formato HTML en el puerto 3000.

El contenedor Docker se construirá a partir de una imagen basada en **Amazon Linux 2023** y usará **nginx** como servidor web para servir la aplicación Node.js.

---

## Modo de Uso

### Pre-requisitos
* Tener **Docker** instalado en tu sistema.
* Opcional: Un entorno **Linux** o **Mac** es recomendado para una experiencia más fluida, pero también puede ejecutarse en **Windows** con Docker Desktop.

---

## Comenzando la Actividad

***Ejemplo***

### Paso 1: Clona este repositorio en tu máquina local:
```bash
git clone git@github.com:cybercharly/madeo07_act1.git
cd docker_con_aplicacion_nodejs
```
### Paso 2: Construir la Imagen Docker
```bash
docker build -t nodejs-hola-mundo .
```
### Paso 3:  Ejecutar el Contenedor
```bash
docker run -p 3000:3000 nodejs-hola-mundo
```

**Salidas de Pantalla**
| Nombre | Descripcion |
|------|-------------|
| HTTP Status | Código de estado 200 para respuestas exitosas |
| Contenido | Mensaje "Hola Mundo" en formato HTML |
| Puerto | La aplicación escucha en el puerto 3000 |
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
* Se agregó el código de la aplicación en Node.js.
* Se agregó el Dockerfile para construir y ejecutar la aplicación.
* Se agregó el README.md con las instrucciones.
