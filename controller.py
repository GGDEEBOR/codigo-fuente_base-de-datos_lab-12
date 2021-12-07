from index import *
from flask import render_template

#loging
@app.route('/Login')
def Login():
    return render_template('Login.html')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/Grados_academicos')
def grados_academicos():
    return render_template('Mensaje.html')



#agregar contacto
@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
       fullname = request.form['fullname']
       lastname = request.form['lastname']
       email = request.form['email']
       phone = request.form['phone']
       cur = mysql.connection.cursor()
       #cur.(SELECT *FROM flaskcontacts)
       cur.execute('INSERT INTO data_base_compra (fullname,lastname,  phone, email) VALUES (%s, %s, %s)', (fullname,lastname,  email, phone))
       mysql.connection.commit()
       return render_template('home.html')


       


