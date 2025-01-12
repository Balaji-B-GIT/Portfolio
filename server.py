import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect, send_from_directory
import smtplib

# load_dotenv("C:/Python/Environmental variables/.env")
my_mail = "sampleforpythonmail@gmail.com"
# run locally, you need to install dot env "pip install python-dotenv" and uncomment below code.
# password = os.getenv("smtp_app_password")
# for hosting online, use below line.
password = os.environ.get("APP_PASSWORD")

app = Flask(__name__)
# for hosting online, use below line.
# If 404 error occurs, change the below secret key
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/downloadable_resume")
def download():
    return send_from_directory(directory="static",path="assets/res/resume.pdf")

@app.route('/',methods=["POST","GET"])
def contact():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs=my_mail,
                                msg=f"Subject:Message from Portfolio\n\n"
                                    f"Name : {data['name']}\n"
                                    f"Email : {data['email']}\n"
                                    f"Message : {data['message']}")
        return redirect(url_for('home'))
if "__main__" == __name__:
    app.run(debug=True)