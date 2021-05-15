# import sqlite3
#
# print('sqlite3.version', sqlite3.version)
#
# conn = sqlite3.connect('d:\program files\sqlite_db\mydb.db')
#
# c = conn.cursor()
# print('cursor type', type(c))
import datetime


class Foo:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print('I am ' +self.name)

class Bar(Foo):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print('You are ' + self.name)


bar = Bar('john')
bar.speak()

ss=''
ss += '2d'
print(ss)

def int_sum(*args):
    ssum =''

    try:
        for n in args:
            print('n=', n, type(args))
            ssum *= n
            print(ssum)
    except Exception :
        print('exc', Exception)
    return ssum

(int_sum('1','2'))

import sqlite3
#'%y-%m-%d %H:%m:%s'
now = datetime.datetime.now()
now2 = now.strftime('%Y-%m-%d %H:%M:%S')
print(now)
print(now2)
