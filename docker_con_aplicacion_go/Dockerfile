# Usar una imagen oficial de Amazon Linux 2023
FROM amazonlinux:2023

# Instalar Go
RUN yum update -y && \
    yum install -y golang && \
    yum clean all

# Crear un directorio de trabajo
WORKDIR /app

# Copiar el código fuente al contenedor
COPY main.go /app/

# Compilar la aplicación
RUN go build -o app main.go

# Exponer el puerto 8080 (estándar para aplicaciones Go)
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["./app"]
