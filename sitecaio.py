from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)
@app.route("/regras")
def entrar():
    return render_template("regras.html")

@app.route("/logar")
def logar():
    return render_template("logar.html")

@app.route("/inscricao")
def inscricao():
    return render_template("inscricao.html")
@app.route("/entrar")
def entrar():
    return render_template("entrar.html")
@app.route("/submit_registration", methods=["POST"])
def submit_registration():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    mensagem = request.form.get("mensagem")

    # Dados do email
    sender_email = "seu_email@gmail.com"
    receiver_email = "caioba.maciel@gmail.com"
    password = "sua_senha_de_app"  # Ou a senha da sua conta, se permitido

    subject = "Novo Formulário de Inscrição"
    body = f"""
    Nome: {nome}
    Email: {email}
    Senha: {senha}
    Mensagem: {mensagem}
    """

    # Construir o email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Enviar o email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email enviado com sucesso")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

    # Redirecionar para a página inicial ou outra página após o envio
    return redirect(url_for("homepage"))

if __name__ == "__main__":
    app.run(debug=True)

