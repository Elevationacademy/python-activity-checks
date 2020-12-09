import sqlite3
import os

class CakesDb:
    def __init__(self, dbfile):
        # make sure we remove previous file since we made changes on it after previous sessions.
        print("Openning ", dbfile)
        if os.path.exists(dbfile):
            os.remove(dbfile)
        self.conn = sqlite3.connect(dbfile)
        print("Openned ", dbfile)

    def populateDb(self, scriptfile):
        f = open(scriptfile, "r")
        query = f.read()
        c = self.conn.cursor()
        c.executescript(query)
        # Save (commit) the changes
        self.conn.commit()
        c.close()

    def select_query(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        names = [description[0] for description in cur.description]
        rows = cur.fetchall()
        return names, rows

    def exec_query(self, query):
        c = self.conn.cursor()
        c.executescript(query)

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()

solution_cakes_db = CakesDb('CakesDb.sqlite')
solution_cakes_db.populateDb(os.path.dirname(__file__) + '/CakesDatabaseSqlite.sql')

