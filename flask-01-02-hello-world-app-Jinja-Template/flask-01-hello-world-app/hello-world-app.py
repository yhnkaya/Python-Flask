from flask import Flask
app = Flask(__name__)
@app.route("/")
def head():
    return "Welcome!"
@app.route("/second")
def second():
    name = "Elyes"
    return f"My name is {name}"
@app.route('/third/subthird')
def third():
    return "Returned from subthird endpoint!"
@app.route('/forth/<string:name>')
def forth(name):
    return f"Hello it's {name} again!"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000,debug=False)