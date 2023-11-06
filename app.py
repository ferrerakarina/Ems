from flask import Flask, render_template, request
from flask_mail import Mail, Message
import base64

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('formulario.html')


@app.route('/enviar', methods=['POST'])
def enviar():
    remitente_email = request.form['remitente_email']
    remitente_contrasena = request.form['remitente_contrasena']
    destinatarios = request.form['destinatarios']
    lista_destinatarios = destinatarios.split(',')

    asunto = request.form['asunto']
    apodo = request.form['apodo']
    html = request.form['html']

    # Configurar el correo del remitente
    app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    app.config['MAIL_USERNAME'] = remitente_email
    app.config['MAIL_PASSWORD'] = str(remitente_contrasena)
    mail = Mail(app)

    # Crear el mensaje
    msg = Message(asunto)
    msg.sender = apodo+' <{}>'.format(remitente_email)
    msg.recipients = []  # Dejar vacío, ya que no se utilizará para mostrar destinatarios
    # Convertir lista de destinatarios a conjunto
    msg.bcc = set(lista_destinatarios)
    msg.html = html

    # Enviar el mensaje
    mail.send(msg)

    return "Correo enviado correctamente"


if __name__ == '__main__':
    app.run(debug=True)
