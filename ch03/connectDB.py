import pymysql

def insertStatus(status):
    conn = pymysql.connect(host='localhost', user='bssmMrchoi', password='q1w2e3', db='webapp')
    cur = conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
    cur.execute("insert into record_led(status) values('{0}')".format(status))
    conn.commit()
    conn.close()

