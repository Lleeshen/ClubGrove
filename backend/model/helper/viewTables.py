import psycopg2
import psycopg2.extras
from .. import startdb as startdb
import logging

LOG = logging.getLogger(__name__)

def viewTable(tableName, **kwargs):
  con = startdb.startdb()
  checkNamestatement = "SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' and table_name=%s LIMIT 1"

  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute(checkNamestatement,(tableName,))
  item = cur.fetchall()
  result = []
  if(len(item) == 0):
    result = 'No table ' + tableName
  else:
    statement = "SELECT *  FROM " + tableName
    cur1 = con.cursor()
    if 'user' in kwargs and kwargs['user']:
      LOG.debug(kwargs['user'])
      statement += """ where name in 
      (select name from memberships where email =%s
      union 
      select name from requests where email =%s
      union
      select name from interested where email =%s)"""
      cur1.execute(statement,(kwargs['user'],kwargs['user'],kwargs['user'],))
    else:
      cur1.execute(statement)
    item1 = cur1.fetchall()
    column = [desc[0] for desc in cur1.description]
    for row in item1:
        result.append(dict(zip(column,row)))
    cur1.close()
  cur.close()
  con.close()
  return result
