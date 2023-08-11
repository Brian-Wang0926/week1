from flask import Flask,render_template,redirect,request,session,json
import mysql.connector
import os
from dotenv import load_dotenv

# 將敏感資訊移至.env
load_dotenv()
mysql_password = os.environ.get('MYSQL_PASSWORD')
mysql_host = os.environ.get('MYSQL_HOST')
mysql_user = os.environ.get('MYSQL_USER')
mysql_db = os.environ.get('MYSQL_DB')
secret_key = os.environ.get('SECRET_KEY')

app=Flask(__name__,static_folder="static",static_url_path="/static")
app.secret_key = secret_key

# 建置 MYSQL
db_config = {
    'host': mysql_host,
    'user': mysql_user,
    'password': mysql_password,
    'database': mysql_db
}
db = mysql.connector.connect(**db_config) # ** 代表將db_config字典unpacking成 key=value

# 建立資料庫操作函數
def execute_query(query, params = None):
    cursor = db.cursor(dictionary = True)
    cursor.execute(query, params)
    db.commit()
    cursor.close()

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
        cursor.close()
        return redirect(f"/error?message={error_message}")
    else:
        cursor.execute("INSERT INTO member(name, username, password) values(%s, %s, %s)",(name,username,password))
        db.commit()
        cursor.close()
        return redirect("/")

@app.route("/signin",methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM member WHERE username=%s and password=%s"
    cursor.execute(query,(username,password))
    user = cursor.fetchone()
    cursor.close()
    if user:
        session['USER_ID'] = user['id']
        session['NAME'] = user['name']
        session['USERNAME'] = user['username']
        return redirect("/member")
    else:
        error_message="帳號或密碼輸入錯誤"
        return redirect(f"/error?message={error_message}")

@app.route("/member")
def member():
    cursor = db.cursor(dictionary=True)
    query = "select member.name, message.content, message.id from message inner join member on message.member_id=member.id ORDER BY message.id DESC;"
    cursor.execute(query)
    messages = cursor.fetchall()
    cursor.close()

    # 若沒有登入session，則跳回首頁
    name = session.get('NAME')
    if name is None:
        return redirect("/")
    return render_template("success.html", name = name, messages = messages)

@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html",message=message)

@app.route("/signout")
def signout():
    session.pop('USER_ID', None)
    session.pop('NAME', None)
    session.pop('USERNAME', None)
    return redirect("/")

@app.route("/createMessage",methods = ["POST"])
def createMessage():
    content = request.form["message"]
    member_id = session['USER_ID']

    query = "INSERT INTO message(member_id,content)values(%s,%s)"
    execute_query(query,params=(member_id,content))
    return redirect("/member")

@app.route("/deleteMessage",methods=["POST"])
def deleteMessage():
    message_id = request.form["message_id"]
    query = "DELETE FROM message WHERE id=%s;"
    execute_query(query, params=(message_id,))
    return redirect("/member")

if __name__ == '__main__':
    app.run(debug = True, port = 3000)
