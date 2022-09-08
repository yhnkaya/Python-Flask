from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def head():
    message = "Don't worry!..."
    return render_template("index.html", message=message, object=[1,2,3,4,5])


@app.route('/home')
def header():
    object= ["Jack", "Alex", "Fred"]
    return render_template("body.html", object=object)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3003, debug= False)