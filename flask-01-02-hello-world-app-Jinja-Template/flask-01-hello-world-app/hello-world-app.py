from flask import Flask

app = Flask(__name__)

# endpoints

@app.route("/")
def head():
    return "<h1>Hello World</h1>"

@app.route("/second")
def second():
    return "this is the second page"

@app.route("/third")
def third():
    return '{"msg": "this is the third page", "status": 200}'

@app.route("/forth/<string:id>")
def forth(id):
    return f"Hello {id}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 3000, debug= False)