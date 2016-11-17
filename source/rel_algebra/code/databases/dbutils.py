from collections import namedtuple

def csv2dbtable(tablename, csvfields, csvrecords):
    def convert_field(f):
        try:
            return int(f)
        except:
            try:
                return float(f)
            except:
                return f
            
    fields = csvfields.strip().split(';')

    records = []
    for l in csvrecords.strip().split('\n'):
        record = [convert_field(f) for f in l.strip().split(';')]
        records.append(record)
 
    RecordClass = namedtuple(tablename, fields)
    table = [RecordClass._make(r) for r in records]

    return table

def dbtable2html(relation):
    def th(relation):
        html = '<tr class="dbtable">\n'
        for f in relation[0]._fields:
            html += '<th class="dbtable">'
            html += f
            html += '</th>\n'
        html += '</tr>\n'

        return html

    evenodd = ['even', 'odd']
    def tr(record, evenodd):
        html = '<tr class="{}">\n'.format(evenodd)
        
        for i, c in enumerate(record):
            html += '<td class="dbtable">'
            html += str(c)
            html += '</td>\n'
        html += '</tr>\n'

        return html
        
    html = '<table class="dbtable">\n'

    if len(relation) == 0:
        html += 'Table vide'
    else:
        html += th(relation)

        evenodd = ['even', 'odd']
        for i, record in enumerate(relation):
            html += tr(record, evenodd[i%2])

    html += '</table>\n'

    return html
    

if __name__ == '__main__':
    # Données de base au format CSV
    csvetudiants = '''
    1;Einstein;Albert;albert@physics.net;Physique;14-03-1879;m
    2;Turing;Allan;turing@lambda.net;Mathématiques;23-06-1912;m
    3;Von Neumann;John;john@gametheory.com;Mathématiques;28-12-1903;m
    4;Van Rossum;Guido;Guido@gmail.com;Informatique;31-01-1956;m
    5;Hopper;Grace;grace.hopper@compilers.org;Informatique;09-12-1906;f
    '''

    table_etudiants = csv2dbtable(
        'Etudiant',
        'no_etudiant;nom;prenom;courriel;os;naissance;sexe',
        csvetudiants)

    print(table_etudiants)
