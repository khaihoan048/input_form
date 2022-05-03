from flask import Flask,render_template, request
from flaskext.mysql import MySQL

app=Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

app.config['MYSQL_DATABASE_USER'] = 'khaihoan'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Kh04082002'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql=MySQL(app)

@app.route('/', methods=['POST'])
def signup():
    _token=request.form['inputToken']
    _email = request.form['inputEmail']
    if len(_token)!=32: 
        return "Invalid token"
    if _email and _token:
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("insert into userinfo (email,token) VALUES ('%s','%s')"%(_email,_token))
        con.commit()
        cur.close()
        return "Success!"

    else:
        return "Fail!"
  


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
