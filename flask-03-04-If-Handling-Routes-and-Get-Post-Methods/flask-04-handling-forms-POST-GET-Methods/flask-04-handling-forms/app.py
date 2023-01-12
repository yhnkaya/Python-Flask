# Import Flask modules
from flask import Flask, redirect, url_for, render_template, request
# Create an object named app
app = Flask(__name__)
@app.route('/', methods=["POST", 'GET'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(password)
    if password == "clarusway": # if password is clarusway redirect to /greet/username
        return redirect(url_for("greet", name= username))
    elif (username == "admin") and (password == "admin"): # if password and username are admin then send the secure html page
        return render_template("secure.html", user = username)
    elif username: # if only the username is sent or the password is wrong the refresh the page with the hint
        return render_template("login.html", control=True, user= username)
    else: # similate a refresh
        return render_template("login.html")
@app.route("/greet/<name>") # greeting page that the user will hit a result of a redirection
def greet(name):
    return render_template("greet.html", user=name)
@app.route('/main') # remember to send param query "name" ==> http://127.0.0.1:3000/main?name=userName
def main():
    namep = request.args.get("name")
    return render_template("main.html", name= namep)
if __name__ == '__main__':
    app.run(port=3000, debug=True)