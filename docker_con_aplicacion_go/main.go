package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	// Escribir la respuesta
	w.Header().Set("Content-Type", "text/html")
	fmt.Fprint(w, "<!DOCTYPE html><html><head><title>Hola Mundo</title></head><body><h1>Hola Mundo</h1><p>Esto es Go</p></body></html>")
}

func main() {
	// Configurar el servidor
	http.HandleFunc("/", handler)

	port := "8080"
	fmt.Printf("Servidor corriendo en http://0.0.0.0:%s\n", port)

	// Iniciar el servidor en el puerto 8080
	if err := http.ListenAndServe("0.0.0.0:"+port, nil); err != nil {
		panic(err)
	}
}
