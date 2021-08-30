import os, sqlite3, datetime

def connect_databse():
    # print(os.path.dirname(os.path.realpath(__file__)))
    conn = sqlite3.connect("./logs.db")
    return conn

def CreateTable(tabletype):
    try:
        tables = {
            "template":'CREATE TABLE IF NOT EXISTS templates (time TEXT,frompath TEXT,topath TEXT);'
        }
        conn = connect_databse()
        c = conn.cursor()
        c.execute(tables[tabletype])
        c.close()
        return True
    except:
        return False

def LogTemplate(frompath, topath, templatetime=None):
    conn = connect_databse()
    if templatetime == None:
        templatetime = str(datetime.datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))
    if conn:
        CreateTable("template")
        c = conn.cursor()
        insertcommand = 'INSERT INTO templates(time, frompath, topath) VALUES(?,?,?)'
        c.execute(insertcommand, (templatetime, frompath, topath))
        conn.commit()
        c.close()
        return True
