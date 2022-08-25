from flask import Flask, render_template

app = Flask(__name__)




@app.route("/home")
def home():
    return render_template("index.html", name="Elyes", lastname="Ferjani")

# endpoint sum
# /sum/10/20 ==> 30

@app.route("/sum/<int:x>/<int:y>")
def calculate(x, y):
    return render_template("body.html",x=x, y=y, sum= x + y)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080, debug= False)