from flask import render_template, request
from flask_mail import Message, Mail
from app import app

mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'markp862@gmail.com'
app.config["MAIL_PASSWORD"] = "appPassword"

mail.init_app(app)

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/portfolio')
def portfolio():
	return render_template("portfolio.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact', methods=["GET","POST"])
def contact():
	email = {}

	if request.method == "POST":
		email["name"] = request.form.get("name")
		email["sender"] = request.form.get("email")
		email["subject"] = request.form.get("subject") 
		email["message"] = request.form.get("message")

		msg = Message(email["subject"], sender=email["sender"], recipients=['markp862@gmail.com'])
		msg.body = """
		From: %s <%s>
		%s
		""" % (email["name"], email["sender"], email["message"])
		mail.send(msg)

	return render_template("contact.html")