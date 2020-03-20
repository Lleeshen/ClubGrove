from urllib.parse import urlparse

def info(**kwargs):

    con = startdb.startdb()
    if 'name' not in kwargs: 
        return None
    checkNamestatement = """
    SELECT * from memberships where name = %s
    """
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(checkNamestatement,)
    result = []
    item = cur.fetchall()

    column = [desc[0] for desc in cur.description]
    for row in item:
        result.append(dict(zip(column,row)))
    cur.close()
    con.close()
    return result