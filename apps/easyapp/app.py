import os
from flask_mail import Mail , Message
from flask import Flask , render_template , url_for , redirect , request , flash
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)

app.config["SECRET_KEY"] = b'4\xfapo\x80B\xaec2\x81\xc9\n\xbf\t\xdd\xc8'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jojju486@gmail.com'
app.config['MAIL_PASSWORD'] = 'stkm cgck saeq hlju'

mail = Mail(app)

@app.route("/")
def index():
    return 'Hello, 성공!!!'

@app.route("/hello/<name>",methods = ["GET"],endpoint='hello-enepoint')
def hello(name):
    return f"hello!! {name}!!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",name=name)

def send_email(to, subject, template, **kwargs):    

    """메일을 송신하는 함수"""

    msg = Message(subject, sender='jojju486@gmail.com', recipients=[to])

    msg.body = render_template(template + ".txt", **kwargs)

    msg.html = render_template(template + ".html", **kwargs)

    mail.send(msg)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact_complete",methods = ["GET","POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True

        if not username:
            flash("사용자명은 필수입니다.")
            is_valid = False

        if not email:
            flash("메일 주소는 필수입니다.")
            is_valid = False
            try:
                validate_email(email)
            except EmailNotValidError:
                flash("메일 주소의 형식으로 입력하세요.")
                is_valid = False

        if not description:
            flash("문의 내용은 필수입니다.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))
        
        send_email(email,"문의 감사합니다.","contact_mail",username = username,description = description)
        flash("문의 내용은 메일로 송신했습니다. 문의해 주셔서 감사드립니다.")

        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

with app.test_request_context():
    print(url_for("index"))
    print(url_for("show_name",name='choyj',page=1))
    print(url_for("index"))