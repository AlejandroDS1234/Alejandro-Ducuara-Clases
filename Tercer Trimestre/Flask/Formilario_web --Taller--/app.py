from flask import Flask, render_template, flash, request, redirect, url_for
import psycopg2 as pys

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

@app.route('/')
def index():
    return render_template('index.html')


def conexion_db():
    try:
        conexion = pys.connect(
            host="localhost",
            port="5432",
            user="postgres",
            password="123456",
            dbname="formulario"
        )
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None
    
@app.route('/procesar', methods=['POST'])
def procesar():
    if request.method == 'POST':
        conexion = conexion_db()
        if conexion is None:
            flash("Error al conectar a la base de datos", "danger")
            return redirect(url_for('index'))
        cursor = conexion.cursor()
        
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo = request.form['email']
        mensaje = request.form['mensaje']
        
        consulta = "INSERT INTO datos_formulario (nombre, apellido, direccion, telefono, correo, mensaje) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(consulta, (nombre, apellido, direccion, telefono, correo, mensaje))
        conexion.commit()
        cursor.close()
        flash("Formulario procesado correctamente", "success")
        return redirect(url_for('index'))
    else:
        flash("Error al procesar el formulario", "danger")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
