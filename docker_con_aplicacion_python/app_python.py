from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<!DOCTYPE html><html><head><title>Hola Mundo</title></head><body><h1>Hola Mundo, esto es Python</h1></body></html>")

if __name__ == "__main__":
    server_address = ('', 8000)  # Escucha en el puerto 8000
    httpd = HTTPServer(server_address, HelloWorldHandler)
    print("Servidor corriendo en http://0.0.0.0:8000")
    httpd.serve_forever()
