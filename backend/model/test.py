import psycopg2
import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dbfile.ini'))


con = psycopg2.connect(dbname=parser.get('postgres','dbname'),
  user=parser.get('postgres','user'),
  host=parser.get('postgres','host'),
  password= parser.get('postgres', 'password'))
cur = con.cursor()
cur.execute("insert into ok values (1, 't', 'stuff')")
cur.execute("select * from ok")
item = cur.fetchall()
print(item)
cur.close()
con.close()
