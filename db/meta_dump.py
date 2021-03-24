import sqlite3
import csv
from dataclasses import dataclass

#RE: public static class GameDefine {}
RESOURCE_SERVER_URL = 'https://prd-storage-umamusume.akamaized.net/dl/resources'
PLATFORM = '/Android' #'/iOS' for iOS / '/Windows' for DMM
ASSETBUNDLES = RESOURCE_SERVER_URL + PLATFORM + '/assetbundles/{0:.2}/{0}'
GENERIC = RESOURCE_SERVER_URL + '/Generic/{0:.2}/{0}'
MANIFEST = RESOURCE_SERVER_URL + '/Manifest/{0:.2}/{0}'

@dataclass
class DataRow():
    '''meta db data class

    meta db column definition:
        i,n,d,g,l,c,h,m,k,s,p
        id,name,?,?,size,checksum,hname,manifest,kind,?,?
    '''
    name: str
    size: int
    checksum: int
    hname: str
    manifest: str
    kind: int
    def getUrl(self):
        '''Return the corresponding url.

        column 'k' in meta db:
            0: assetbundles
            1: manifest
            2: manifest2
            3: manifest3
            10: master
            11: sound (criware acb/awb)
            12: movie (criware usm)
            13: font
        * 10, 11, 12, 13 -> GENERIC
        * 1, 2, 3 -> MANIFEST
        * 0 -> ASSETBUNDLES
        '''
        url = ''
        if self.kind == 0:
            url = ASSETBUNDLES.format(self.hname)
        elif self.kind in [1, 2, 3]:
            url = MANIFEST.format(self.hname)
        elif self.kind in [10, 11, 12, 13]:
            url = GENERIC.format(self.hname)
        else:
            url = 'rua'
        return url
    def __str__(self):
        return self.name

def readDB(dbpath: str) -> list:
    db_list = []
    con = sqlite3.connect(dbpath)
    cursor = con.cursor()
    for row in cursor.execute('SELECT "n", "l", "c", "h", "m", "k" FROM "a"'): #60000+ rows LIMIT ¯\_(ツ)_/¯
        db_row = DataRow(*row)
        if db_row.name.startswith('//'):
            db_row.name = f'{db_row.manifest}/{db_row.name[2:]}'
        db_list.append(db_row)
    return db_list

def exportCSV(dblist: list, filepath: str):
    with open(filepath, 'w', encoding='utf-8-sig', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(['name', 'url'])
        for db_row in dblist:
            csv_writer.writerow([db_row, db_row.getUrl()])
    
if __name__ == '__main__':
    dblist = readDB('db/meta')
    exportCSV(dblist, 'meta.csv')