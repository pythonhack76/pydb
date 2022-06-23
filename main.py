import sqlite3

connection = sqlite3.connect("clienti.db")
cursor = connection.cursor()



clienti_list = [
    (2000, "cliente1", "abbigliamento"),
    (2001, "cliente2", "consulenza"),
    (2002, "cliente3", "studio legale"),
    (2003, "cliente4", "farmacia"),
    (2004, "cliente5", "metalmeccanica"),
    (2005, "cliente6", "plastica"),
    (2006, "cliente7", "software")
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

connection.close() 