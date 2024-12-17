# Usar la imagen base oficial de Amazon Linux 2023
FROM amazonlinux:2023

# Instalar Node.js y npm
RUN yum update -y && \
    curl -sL https://rpm.nodesource.com/setup_18.x | bash - && \
    yum install -y nodejs && \
    yum clean all

# Crear el directorio de la aplicación
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY package*.json /app/
COPY app_node.js /app/app.js

# Instalar las dependencias de la aplicación
RUN npm install

# Exponer el puerto por defecto para Node.js (3000)
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["node", "app.js"]
