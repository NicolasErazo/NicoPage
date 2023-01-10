from flask import Flask
from flask import render_template, request, redirect
import smtplib
from decouple import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')    

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/blog')
def blog():
    return render_template('/blog.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')  

@app.route('/contact/save', methods=['POST'])
def save_contact_and_send_email():

    name =  request.form['name']
    email =  request.form['email']
    phoneNumber =  request.form['phoneNumber']
    message =  request.form['message']
    subject = "Contact Us"

    messageEmail = 'Subject: {}\n\n {} quiere contactarse contigo a travez del correo: {}\n\nSu numero de contacto es: {}\n\nSu mensaje: {}'.format(subject, name, email, phoneNumber, message)

    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.starttls()
    server.login("nico.lacho@outlook.com", "Nicolaserazo1")
    server.sendmail("nico.lacho@outlook.com", "nico.lacho@outlook.com", messageEmail)
    server.quit()

    return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True)      
