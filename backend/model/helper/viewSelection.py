import psycopg2
import psycopg2.extras
from .. import startdb as startdb

def viewRow(tableName,name):
  con = startdb.startdb()

  checkNamestatement = "SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' and table_name=%s LIMIT 1"

  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(checkNamestatement,(tableName,))
  item = cur.fetchall()
  result = []
  tableid =""
  if(len(item) == 0):
    result = 'No table ' + tableName
  else:
    #note got this off a wiki Just grabs the primary key
    pStatement = "SELECT a.attname \
                  FROM   pg_index i\
                  JOIN   pg_attribute a ON a.attrelid = i.indrelid\
                     AND a.attnum = ANY(i.indkey)\
                  WHERE  i.indrelid =%s::regclass\
                  AND    i.indisprimary;"
    cur2 = con.cursor()
    cur2.execute(pStatement,(tableName,))
    tableid = cur2.fetchone()

    statement = "SELECT *  FROM " + tableName +" WHERE "+ tableid[0]+ " = %s"
    cur1 = con.cursor()
    cur1.execute(statement,(name,))
    item1 = cur1.fetchone()
    column = [desc[0] for desc in cur1.description]
    if (item1 != None):
        result.append(dict(zip(column,item1)))
    cur1.close()
  cur.close()
  con.close()
  return result