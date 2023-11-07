import pymysql

num=4
conn = pymysql.connect(host='localhost', user='bssmMrchoi', password='q1w2e3', db='ch02')
cur = conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
cur.execute("insert into numcount(num) values({0})".format(num));
conn.commit()
conn.close()
