from ntpath import join
import os, sqlite3, datetime, CleverTemplateErrors, json
from tabulate import tabulate
mainpath = os.path.dirname(os.path.realpath(__file__))
tables = {
    "templates":'CREATE TABLE IF NOT EXISTS templates (time TEXT,frompath TEXT,topath TEXT, data TEXT);'
}
def connect_databse():
    conn = sqlite3.connect(os.path.join(mainpath, "logs.db"))
    conn.row_factory = dict_sql
    return conn

def dict_sql(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def CreateTable(tabletype):
    try:
        c = connect_databse().cursor()
        c.execute(tables[tabletype])
        c.close()
        return True
    except:
        return False

def LogTemplate(frompath, topath, data, templatetime=None):
    conn = connect_databse()
    if templatetime == None:
        templatetime = str(datetime.datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))
    if conn:
        CreateTable("templates")
        c = conn.cursor()
        insertcommand = 'INSERT INTO templates(time, frompath, topath, data) VALUES(?,?,?,?)'
        c.execute(insertcommand, (templatetime, frompath, topath, data))
        conn.commit()
        c.close()
        return True
    return False

def ReadLog(logtype):
    if logtype in tables:
        conn = connect_databse()
        c = conn.cursor()
        exist = c.execute("select count(*) from sqlite_master where type='table' and name=?", (logtype,)).fetchall()
        if exist[0]['count(*)'] != 0:
            return c.execute(f"SELECT * FROM {logtype}",).fetchall()
    raise CleverTemplateErrors.LogTypeDoesNotExist(logtype, ListLogs())

def ListLogs():
    c = connect_databse().cursor()
    return c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

def WriteLogs(path, logtype):
    if os.path.exists(path):
        n = ""
        while True:
            fullpath = os.path.join(path, f"ct-log-{logtype}{n}.txt")
            if os.path.isfile(fullpath) and os.path.exists(fullpath):
                if type(n) == str:
                    n = 1
                else:
                    n += 1
            else:
                break
        try:
            c = connect_databse().cursor()
            c.execute("SELECT name FROM PRAGMA_TABLE_INFO('templates');")
            rowtopraw = c.fetchall()
            topraw = list()
            enddata = list()
            for top in rowtopraw:
                topraw.append(top["name"])
            enddata.append(topraw)
            data = ReadLog(logtype)
            for part in data:
                partlist = list()
                for p in part:
                    partlist.append(str(part[p]))
                enddata.append(partlist)
            writedata = [" - ".join(partdata) for partdata in enddata]
            open(fullpath, "w+").write("\n".join([d for d in writedata]))
            return fullpath
        except Exception as e:
            raise CleverTemplateErrors.ErrorWhenTryingToWriteInFile(fullpath)