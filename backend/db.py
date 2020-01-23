import psycopg2

con = psycopg2.connect(dbname='testing', user='postgres',
        host='localhost', password= '')
cur = con.cursor()
cur.execute("insert into ok values (1, 't', 'stuff')")
cur.execute("select * from ok")
item = cur.fetchall()
print("connected.",item)
cur.close()
con.close()