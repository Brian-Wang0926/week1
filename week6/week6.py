from flask import Flask,render_template,redirect,request,session,json
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.environ.get('MYSQL_PASSWORD')

app=Flask(__name__,static_folder="static",static_url_path="/")
app.secret_key="any string but secret"

# 建置 MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = db_password
app.config['MYSQL_DB'] = 'website'

db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup",methods=['POST'])
def signup():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']


    # 檢查是否有重複 username，若有導向失敗頁面，若無導向首頁
    cursor = db.cursor()
    cursor.execute("SELECT * FROM member WHERE username=%s",(username,))
    existing_user = cursor.fetchone()
    if existing_user:
        error_message="帳號已經被註冊"
        return redirect("/error?message="+error_message)
    else:
        cursor.execute("INSERT INTO member(name, username, password) values(%s, %s, %s)",(name,username,password))
        db.commit()
        cursor.close()
        return redirect("/")

@app.route("/signin",methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    cursor = db.cursor()
    cursor.execute("SELECT * FROM member WHERE username=%s and password=%s",(username,password))
    user = cursor.fetchone()
    if user:
        user_id = user[0]
        name = user[1]
        username = user[2]
        session['USER_ID'] = user_id
        session['NAME'] = name
        session['USERNAME'] = username
        return redirect("/member")
    else:
        error_message="帳號或密碼輸入錯誤"
        return redirect("/error?message="+error_message)

@app.route("/member")
def member():
    cursor = db.cursor()
    cursor.execute("select member.name, message.content, message.id from message inner join member on message.member_id=member.id ORDER BY message.id DESC;")
    show_message = cursor.fetchall()

    # 顯示留言
    message_lists=[]
    for message in show_message:
        message_list = f"{message[0]}:{message[1]}:{message[2]}"
        message_lists.append(message_list)
    print(message_lists)

    # 若沒有登入session，則跳回首頁
    name = session.get('NAME')

    if name is None:
        return redirect("/")
    return render_template("success.html", name=name, message=message_lists)

@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("error.html",message=message)

@app.route("/signout")
def signout():
    session.pop('USER_ID', None)
    session.pop('NAME', None)
    session.pop('USERNAME', None)
    return redirect("/")

@app.route("/createMessage",methods=["POST"])
def createMessage():
    content = request.form["message"]
    member_id = session['USER_ID']
    cursor = db.cursor()
    cursor.execute("INSERT INTO message(member_id,content)values(%s,%s)",(member_id,content))
    db.commit() 
    return redirect("/member")

@app.route("/deleteMessage",methods=["POST"])
def deleteMessage():
    message_id = request.form["message_id"]
    cursor = db.cursor()
    cursor.execute("DELETE FROM message WHERE id=%s;",(message_id,))
    db.commit()
    return redirect("/member")


if __name__ == '__main__':
    app.run(debug=True,port=3000)
