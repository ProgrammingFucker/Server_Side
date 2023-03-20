
from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_mysqldb import MySQL
from MySQLdb.cursors import Cursor

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'almacen'

mysql = MySQL(app)

app.secret_key = ";:_"
    

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    msg = ''
    if request.method == 'POST':
        email = request.form['txt_Correo']
        password = request.form['txtPassword']
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM login where correo = %s AND password = %s', (email, password))
        user = cursor.fetchone()
        if user:
            return redirect(url_for('route_admin'))
        else:
            msg = 'Credenciales Incorrectas!'
            return render_template('login.html', msg=msg)


@app.route('/route_admin')  # Administrador
def route_admin():
    sql = "SELECT * FROM empleados"
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    empleados = cursor.fetchall()
    print(empleados)
    cursor.close()
    return render_template('home.html', number=empleados)



@app.route('/edit')  # Ruta Editar elementos sql
def edit():
    return render_template('editar.html')


@app.route('/editar/id>', methods=['POST'])  # Editar elementos sql
def editar(id):
    msg = ''
    if request.methods == 'POST':
        no_emp = request.form['no_emp']  # id
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        salario = request.form['salario']
        genero = request.form['genero']
        celular = request.form['celular']
        # No se puede actualizar porque son datos básicos únicos de la persona
        ciudad = request.form['ciudad']
        # No se puede actualizar porque son datos básicos únicos de la persona
        fecha_nac = request.form['f_nac']
        # No se puede actualizar porque son datos básicos únicos de la persona
        fecha_ingreso = request.form['f_ingreso']

  # Editar elementos sql


@app.route('/delete', methods=['POST'])
def delete(id):
    cursor = mysql.connection.cursor()
    with cursor.cursor() as cursor:
        cursor.execute('DELETE * FROM empleados where no_emp ={0}'.format(id))
    cursor.commit()
    flash('Elemento eliminado correctamente')
    return redirect(url_for('route_admin'))
    cursor.close()






if __name__ == '__main__':
    app.run(port=3000, debug=True)

