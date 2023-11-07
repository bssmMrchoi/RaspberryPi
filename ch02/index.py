from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<num>")
def up(num):
    conn = pymysql.connect(host='localhost', user='bssmMrchoi', password='q1w2e3', db='ch02')
    cur = conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
    cur.execute("insert into numcount(num) values({0})".format(num));
    conn.commit()
    conn.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
