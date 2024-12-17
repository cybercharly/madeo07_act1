# app.py - Aplicación en Flask que muestra los datos de la base de datos SQLite

from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    # Conectar con la base de datos SQLite
    conn = sqlite3.connect('/data/person.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")
    person = cursor.fetchone()
    conn.close()

    # Mostrar los datos de la persona en un mensaje HTML
    if person:
        return f"<h1>Hola, {person[0]}!</h1><p>Email: {person[1]}</p>"
    else:
        return "<h1>No se encontraron datos en la base de datos.</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
