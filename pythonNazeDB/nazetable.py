from nazedb import NazeDB, DBInfos
import os
import csv


class NazeTable:
    db = ''
    tname = ''
    headers = []
    rows = []

    def __init__(self, tname: str, db: NazeDB):
        self.db = db
        self.tname = tname

        open(self.filepath, 'a+', newline='').close()
        src = open(self.indexpath, 'r', newline='')
        des = open(self.indexpath, 'a', newline='')
        find = 0

        for line in src:
            if line == self.filepath + '\n':
                find = 1
        if find == 0:
            des.write(self.filepath + '\n')
        des.close()
        src.close()

    def set_header(self, ls: [str]):
        self.headers = ls

    def get_header(self) -> [str]:
        return self.headers

    @property
    def filepath(self) -> str:
        return self.db.dbinfos.dbpath + '/' + self.tname + '.csv'

    @property
    def indexpath(self) -> str:
        return self.db.dbinfos.dbpath + '/' + self.db.dbinfos.dbfile

    @property
    def get_rows(self) -> [{str: str}]:
        return self.rows

    def add_row(self, **kw):
        fields = {}
        for key, value in kw.items():
            fields[key] = value
        self.rows.append(fields)

    def save(self):
        tfile = open(self.filepath, 'w', newline='')
        writer = csv.DictWriter(tfile, fieldnames=self.headers)
        writer.writeheader()
        for row in self.rows:
            writer.writerow(row)
        tfile.close()
        return

    def load(self):
        tfile = open(self.filepath, 'r', newline='')
        d_reader = csv.DictReader(tfile)
        self.headers = d_reader.fieldnames
        for row in d_reader:
            self.rows.append(row)
        tfile.close()

    def clean(self):
        os.remove(self.filepath)
        f = open(self.indexpath, "r")
        lines = f.readlines()
        f.close()
        f = open(self.indexpath, "w")
        for line in lines:
            if line != self.filepath + '\n':
                f.write(line)
        f.close()

    @staticmethod
    def cleanall(dbinfos: DBInfos):
        dbpath = dbinfos.dbpath + '/' + dbinfos.dbfile
        f = open(dbpath, "r")
        for line in f:
            os.remove(line.rstrip('\n'))
        f.close()
        f = open(dbpath, "w").close()

        # """supprime toutes les tables associés à une DB. '.index.db' existe mais vide """
