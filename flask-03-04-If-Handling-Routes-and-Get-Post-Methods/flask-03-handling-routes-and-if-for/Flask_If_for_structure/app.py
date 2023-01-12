from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask"

@app.route('/body')
def body():
    return render_template("body.html", object=["John", "James", "Rick"])

@app.route("/message")
def message():
    myMessage = "Hello It's me!"
    myObject = range(0, 10)
    return render_template("index.html", message= myMessage, object= myObject )
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)


