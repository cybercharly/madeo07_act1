const http = require("http");

// Configurar el servidor
const hostname = "0.0.0.0";
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/html");
  res.end("<!DOCTYPE html><html><head><title>Hola Mundo</title></head><body><h1>Hola Mundo</h1><p>Esto es Node.js</p></body></html>");
});

// Iniciar el servidor
server.listen(port, hostname, () => {
  console.log(`Servidor corriendo en http://${hostname}:${port}`);
});
