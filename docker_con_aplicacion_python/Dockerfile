# Usar Amazon Linux 2023 como base
FROM amazonlinux:2023

# Instalar Python3 y herramientas básicas
RUN yum update -y && \
    yum install -y python3 python3-pip && \
    yum clean all

# Crear un directorio de trabajo para la aplicación
WORKDIR /app

# Copiar el script de la aplicación al contenedor
COPY app_python.py /app/app.py

# Exponer el puerto 8000 (puerto por defecto del servidor web de Python)
EXPOSE 8000

# CMD para ejecutar la aplicación
CMD ["python3", "-m", "http.server", "8000", "--bind", "0.0.0.0"]
