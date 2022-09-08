from flask import Flask, render_template, request

def lcm(num1,num2):
    common_multiplications = [] 
    for i in range(max(num1, num2),num1*num2+1):
        if i%num1==0 and i%num2==0:
           common_multiplications.append(i) 
    return min(common_multiplications)

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/calc', methods=['GET','POST'])
def calculate():
    if request.method == 'POST':
        number1= request.form.get("number1")
        number2= request.form.get("number2")
        return render_template("result.html", lcm=lcm(int(number1), int(number2)), result1= number1, result2= number2)
    else: 
        return "<h1> out of reach </h1>"






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003, debug=False)