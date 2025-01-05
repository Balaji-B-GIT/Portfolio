import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for
import smtplib

load_dotenv("C:/Python/Environmental variables/.env")
my_mail = "sampleforpythonmail@gmail.com"
password = os.getenv("smtp_app_password")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/',methods=["POST","GET"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data['name'])
        # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        #     connection.starttls()
        #     connection.login(my_mail, password=password)
        #     connection.sendmail(from_addr=my_mail,
        #                         to_addrs=my_mail,
        #                         msg=f"Subject:Message from Portfolio\n\n"
        #                             f"Name : {data['name']}\n"
        #                             f"Email : {data['email']}\n"
        #                             f"Message : {data['message']}")
    return url_for('home')
if "__main__" == __name__:
    app.run(debug=True)