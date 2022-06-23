

import sqlite3
from tkinter import StringVar


#dati da entry

connection = sqlite3.connect("clienti.db")
cursor = connection.cursor()

cursor.execute("create table IF NOT EXISTS clienti (anno_cliente integer, nome_cliente text, settore_cliente text)")

clienti_list = [
    (2000, "cliente1", "abbigliamento"),
    (2001, "cliente2", "consulenza"),
    (2002, "cliente3", "studio legale"),
    (2003, "cliente4", "farmacia"),
    (2004, "cliente5", "metalmeccanica"),
    (2005, "cliente6", "plastica"),
    (2006, "cliente7", "software"),
    (2009, "cliente8", "abbigliamento")
] 


release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]   

cursor.executemany("insert into clienti values (?,?,?)", clienti_list)


#print database righe
for row in cursor.execute("select * from clienti"):
    print(row)

print("**************************************")
#stampa specifiche righe

cursor.execute("select * from clienti where settore_cliente=:c" , {"c": "abbigliamento"})
clienti_search = cursor.fetchall()
print(clienti_search,'\n')

connection.close() 