# Import Flask modules
from flask import Flask, render_template, request
# Create an object named app
app = Flask(__name__)
# create a function named "lcm" which calculates a least common multiple values of two numbers.
def lcm(num1,num2):
    common_multiplications = []
    for i in range(max(num1, num2),num1*num2+1):
        if i%num1==0 and i%num2==0:
           common_multiplications.append(i)
    return min(common_multiplications)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/calc', methods= ["POST"])
def calc():
    if request.method == "POST":
        num1 = request.form.get("number1")
        num2 = request.form.get("number2")
        lowest = lcm(int(num1), int(num2))
        return render_template("result.html", lcm=lowest, result1= num1, result2= num2, developer_name= "Elyes")
    else:
        return "<h1> Expected a HTTP Post Request <h1>"
if __name__== "__main__":
    app.run(port=3000, debug=True)