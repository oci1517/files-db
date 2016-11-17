## Programme : csv2sql

## auteur : Cédric Donner
## date : mai 2013

## Ce fichier lit un fichier client.csv et crée les requêtes SQL
## INSERT INTO à partir des données contenues dans le fichier csv. Les
## requêtes SQL générées sont écrites dans fichier client_insert.sql

filename = 'client.csv'

def add_quotes(value):
    return "'{}'".format(value)

def escape_quotes(value):
    return value.replace("'", "''")

insert_statements = ''

with open(filename, 'r', encoding='utf-8') as fd:
    first_line = fd.readline()

    fields = first_line.strip().split(';')

    # les lignes suivantes sont des données à transformer en requête
    # INSERT
    query_template = 'INSERT INTO {table} ( {fields} ) VALUES ( {values} );'

    for line in fd:
        values = line.strip().split(';')

        # Faire le traitement nécessaire pour les chaines de caractères
        values = [escape_quotes(v) for v in values]
        values = [add_quotes(v) for v in values]

        query = query_template.format(table='client',
                                      fields=', '.join(fields),
                                      values=', '.join(values))

        print(query)

        insert_statements += query + '\n'

        with open('client_insert.sql', 'w', encoding='utf-8') as fd:
            fd.write(insert_statements)
