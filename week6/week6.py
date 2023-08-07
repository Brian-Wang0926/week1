
from flask import Flask,render_template,redirect,request,session,json
app=Flask(__name__,static_folder="static",static_url_path="/")
app.secret_key="any string but secret"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signin",methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username=='test' and password=='test':
        session['SIGNED-IN'] = True
        return redirect("/member")
    else:
        session['SIGNED-IN'] = False
        error_message=""
        if not username or not password:
            error_message="Please enter username and password"
        else:
            error_message="Username or password is not correct"
        return redirect("/error?message="+error_message)

@app.route("/member")
def member():
    if not session.get('SIGNED-IN'):
        return redirect("/")
    return render_template("success.html")

@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("error.html",message=message)

@app.route("/signout")
def signout():
    session['SIGNED-IN'] = False
    return redirect("/")

@app.route("/square/<int:number>")
def square(number):
    squared=int(number**2)
    return render_template("square.html",number=squared)

if __name__ == '__main__':
    app.run(port=3000)
