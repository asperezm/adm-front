from flask import Flask, render_template, request
import requests

app = Flask(__name__)

PORT = 3200

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/index_results", methods=["GET", "POST"])
def index_results():
 email = request.form.get("email")
 res = requests.get('https://emailverification.whoisxmlapi.com/api/v2?apiKey=at_yHxvRIV7b87JtYvmphqND9xIbZXTI&emailAddress=' + email)
 if res:
    json_result = res.json()
    print(json_result)
    return render_template("index.html", email=json_result)
 else:
    return render_template("index.html", email="ERROR SERVIDOR")

@app.route("/email")
def email():
    return render_template("email_change.html")

@app.route("/update_email", methods=["GET", "POST"])
def update_email():
 email = request.form.get("email")
 newEmail = request.form.get("newEmail")
 res = requests.get('URL' + email + "/" + newEmail)
 if res:
    json_result = res.json()
    return render_template("email_change.html", result=json_result)
 else:
    return render_template("email_change.html", result="ERROR SERVIDOR")

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host='0.0.0.0', port=PORT)