import result as result
from flask import Flask, render_template, jsonify,request

myapp=Flask(__name__)
@myapp.route('/')
def hello():
    return "Hello from my app"
@myapp.route("/hcl")
def index():
    return "developers"
name="liki"
@myapp.route("/home")
def home():
    return render_template("home.html",value=name)
@myapp.route("/demo")
def demo():
    return jsonify(name="liki",place="ban",role="tester")
@myapp.route("/emp")
def emp():
    return render_template("emp.html")
@myapp.route("/result",methods=["POST","GET"])
def result():
    if request.method=="POST":
        result=request.form
        return render_template("result.html",result=result)

