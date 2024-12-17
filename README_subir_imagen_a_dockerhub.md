# Subir Imagen Docker a Docker Hub

Este README te guiará a través de los pasos necesarios para subir una imagen Docker a **Docker Hub**.

## Índice

1. **Pre-requisitos**
2. **Pasos para Subir la Imagen a Docker Hub**
    1. Iniciar sesión en Docker Hub
    2. Construir la Imagen Docker
    3. Etiquetar la Imagen
    4. Subir la Imagen a Docker Hub
3. **Verificación de la Imagen en Docker Hub**

---

## 1. Pre-requisitos

Antes de comenzar, asegúrate de tener lo siguiente:

- **Docker** instalado en tu sistema. Si aún no lo tienes, sigue las instrucciones oficiales para instalar Docker: [Instalar Docker](https://docs.docker.com/get-docker/)
- Una cuenta en **Docker Hub**. Si no tienes una, puedes crearla en: [Crear cuenta en Docker Hub](https://hub.docker.com/signup)

---

## 2. Pasos para Subir la Imagen a Docker Hub

### 2.1. Iniciar sesión en Docker Hub

Primero, abre una terminal y ejecuta el siguiente comando para iniciar sesión en tu cuenta de Docker Hub, Se te pedirá que ingreses tu usuario y contraseña de Docker Hub.

```bash
docker login
```

### 2.2. Construir la Imagen Docker
Una vez que hayas iniciado sesión, ve al directorio donde está tu Dockerfile. Luego, ejecuta el siguiente comando para construir la imagen Docker:
```bash
docker build -t nombre-de-usuario/nombre-de-la-imagen:tag .
```
#### Ejemplo:

***Este comando construye la imagen Docker usando el Dockerfile del directorio actual.***
```bash
docker build -t cybercharly/madeo07_act1_individual:imagen_aplicacion_nodejs .
```
### 2.3. Etiquetar la Imagen

Después de construir la imagen, es necesario etiquetarla correctamente para poder subirla a Docker Hub. Usa el siguiente comando:
```bash
docker tag nombre-de-la-imagen nombre-de-usuario/nombre-de-la-imagen:tag
```
#### Ejemplo:
***Esto etiqueta la imagen nodejs-hola-mundo con el nombre cybercharly/madeo07_act1_individual:imagen_aplicacion_nodejs, que corresponde al formato requerido por Docker Hub.***
```bash
docker tag nodejs-hola-mundo cybercharly/madeo07_act1_individual:imagen_aplicacion_nodejs
```
### 2.4. Subir la Imagen a Docker Hub

Con la imagen etiquetada, ahora puedes subirla a Docker Hub con el siguiente comando:

``` bash
docker push nombre-de-usuario/nombre-de-la-imagen:tag
```

#### Ejemplo
***Este comando subirá la imagen a Docker Hub bajo el nombre de usuario y la etiqueta proporcionados.***
```bash
sudo docker push cybercharly/madeo07_act1_individual:imagen_aplicacion_nodejs
```
## 3. Verificación de la Imagen en Docker Hub

Para verificar que la imagen se haya subido correctamente:

1. Inicia sesión en [Docker Hub](https://hub.docker.com/).
2. Ve a tu perfil de usuario.
3. En la sección "Repositories", busca la imagen que subiste.
4. Verifica que la imagen y la etiqueta estén visibles.
