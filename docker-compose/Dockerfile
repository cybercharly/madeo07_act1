# Dockerfile para la aplicación Python (en la misma carpeta que el docker-compose.yml)
FROM amazonlinux:2023

# Instalar dependencias
RUN yum update -y && \
    yum install -y python3 python3-pip sqlite

# Copiar la aplicación
COPY app.py /app.py

# Instalar Flask y sqlite3
RUN pip3 install Flask sqlite3

# Crear el contenedor para la aplicación
CMD ["python3", "/app.py"]
