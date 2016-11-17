# -*- coding: utf-8 -*-

from dbutils import csv2dbtable

csvrecords = {}
csvfields = {}
ddl = {}

csvfields['CLIENT'] = 'no_client;nom;prenom'
csvrecords['CLIENT'] = '''
1;Turing;Alan
2;Honegger;Arthur
3;Euler;Leonhard
4;Riemann;Berhard
5;von Neuman;John
'''
ddl['CLIENT'] = '''
CREATE TABLE IF NOT EXISTS client
    ( 
        no_client INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(40) NOT NULL,
        prenom VARCHAR(40) NOT NULL
    );
'''

csvfields['COMPTE'] = 'no_compte;montant;date_acces;no_filiale'
csvrecords['COMPTE'] = '''
1;500;01.01.2010;1
2;500;01.01.2010;1
3;700;03.04.2010;4
4;8000;05.07.2010;3
5;6000;05.10.2010;1
6;4000;23.02.2010;1
7;10000;15.04.2010;2
8;2300;12.10.2010;3
9;5600;23.06.2010;2
10;2300;11.10.2010;6
11;5400;01.01.2010;4
'''
ddl['COMPTE'] = '''
    CREATE TABLE IF NOT EXISTS compte
    ( 
        no_compte INTEGER PRIMARY KEY AUTOINCREMENT,
        montant DECIMAL(7,2) NOT NULL DEFAULT 0,
        date_access DATETIME NULL,
        no_filiale_gestion INTEGER NOT NULL,

        FOREIGN KEY (no_filiale_gestion) REFERENCES filiale (no_filiale)
    );
'''

csvfields['POSSESSION'] = 'no_client;no_compte'
csvrecords['POSSESSION'] = '''
1;1
2;1
1;2
2;3
1;4
4;5
2;6
2;7
1;8
4;9
1;10
2;11
'''
ddl['POSSESSION'] = '''
CREATE TABLE IF NOT EXISTS possession
    ( 
        no_compte INTEGER NOT NULL,
        no_client INTEGER NOT NULL,

        -- Clé primaire composée des champs (no_compte, no_client)
        PRIMARY KEY(no_compte, no_client)
    );
'''

csvfields['FILIALE'] = 'ville;no;no_filiale'
csvrecords['FILIALE'] = '''
Bulle;1;1
Fribourg;1;2
Lausanne;1;3
Lausanne;2;4
Zurich;1;5
Zurich;2;6
Zurich;3;7
'''
ddl['FILIALE'] = '''
    CREATE TABLE IF NOT EXISTS filiale
    ( 
        no_filiale INTEGER PRIMARY KEY AUTOINCREMENT,
        ville VARCHAR(20) NOT NULL,
        no INTEGER NOT NULL DEFAULT 1
    );
'''

tables = ['CLIENT', 'FILIALE', 'COMPTE', 'POSSESSION']

def DB():
    R = {}
    for t in tables:
        R[t] = csv2dbtable(t, csvfields[t], csvrecords[t])

    return R

def population(R, table):
    fields = ', '.join(csvfields[table].split(';'))
    for record in R[table]:
        print("INSERT INTO {table} ({fields}) VALUES {values};".format(table=table.lower(),
                                                                         fields=fields,
                                                                         values=tuple(record)))

if __name__ == '__main__':									 
    for t in tables:
        population(DB(), t)
        print()

    R = DB()
    for t in tables:
        for r in R[t]:
            keys = [t.lower() + '.' + f for f in r._asdict().keys()]
            values = r._asdict().values()
            print(dict(zip(keys, values)))

            
            
            
            
