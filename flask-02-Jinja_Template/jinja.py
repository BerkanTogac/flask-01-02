from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1=1234, number2=7896)

@app.route("/cohort16")
def number():
    num1 = 12
    num2 = 11
    return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)

if __name__== "__main__":
    app.run(debug=True, port=30001)
    # app.run(host= '0.0.0.0', port=8081)