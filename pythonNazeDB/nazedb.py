import os
from collections import namedtuple

DBInfos = namedtuple(
    'infos', ['dbname', 'dbpath', 'dbfile'])


class NazeDB:
    infos = None

    def __init__(self, dbname=None):

        if dbname == None:
            pass
        if os.path.exists(dbname):
            dbpath = os.path.relpath(dbname)
            self.infos = DBInfos._make(
                [dbname, './' + dbpath, '.index.db'])
        else:
            dbpath = self.make_db(dbname)
            self.infos = DBInfos._make([dbname, dbpath, '.index.db'])

    def make_db(self, name, path='.'):
        pathdb = path + '/' + name
        os.makedirs(pathdb)
        open(pathdb + '/.index.db', 'a').close()
        return pathdb

    @staticmethod
    def search_db(dbname: str, path='.'):
        find = None
        for root, dirs, files in os.walk(path):
            for basename in dirs:
                if basename == dbname:
                    if os.path.exists(root + '/' + dbname + '/.index.db'):
                        find = root + '/' + dbname
        return find

    def open(self, dbname: str):
        dbpath = self.search_db(dbname)
        if dbpath == None:
            dbpath = self.make_db(dbname)
        self.infos = DBInfos._make([dbname, dbpath, '.index.db'])

    @ property
    def dbinfos(self) -> DBInfos:
        return self.infos

    @ staticmethod
    def listdb() -> [DBInfos]:
        l = []
        for root, dirs, files in os.walk('.'):
            if '.index.db' in files:
                d = DBInfos._make(
                    [os.path.basename(root), root, '.index.db'])
                l.append(d)
        return l
