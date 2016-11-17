from little_bank import tables, DB
from relational_algebra import *

################################################################################
## REQUETES SUR LA BASE DE DONNEES BANQUE
################################################################################

R = DB()

query = OrderedDict()

print(tables)

for t in tables:
    query[t] = R[t]

print(R['CLIENT'])

query['comptes de Allan Turing'] = projection(selection(cartprod(R['CLIENT'], R['POSSESSION']), "r.CLIENT_no_client == r.POSSESSION_no_client and r.CLIENT_nom == 'Turing'"), ['POSSESSION_no_compte'])
query['comptes de Honegger'] = projection(
                                    selection(
                                        cartprod(R['CLIENT'], R['POSSESSION']),
                                        "r.CLIENT_no_client == r.POSSESSION_no_client and r.CLIENT_nom == 'Honegger'"
                                        )
                                    , ['POSSESSION_no_compte']
                                )
query['client no 2'] = selection(R['CLIENT'], 'r.no_client == 2')
query['nom et prénom de la table CLIENT'] = projection(R['CLIENT'], ['nom', 'prenom'])
query['Produit cartésien'] = cartprod(R['CLIENT'], R['COMPTE'])

query['Exercice 1.a 1e étape'] = cartprod(R['CLIENT'], R['POSSESSION'])
query['Exercice 1.a 2e étape'] = selection(query['Exercice 1.a 1e étape'],
                                                 'r.CLIENT_no_client == r.POSSESSION_no_client and r.CLIENT_nom == "Honegger" and r.CLIENT_prenom == "Arthur"')
query['Exercice 1.a 3e étape'] = projection(query['Exercice 1.a 2e étape'], ['POSSESSION_no_compte'])

html_document = '''
<html>
    <head>
        <link type="text/css" rel="stylesheet" href="table.css" />
    </head>
    <body>
    {body}
    </body>
</html>'''

with open('result.html', 'w') as fd:
    html = ''
    for (query, relation) in query.items():
        html += '<h3>' + query + '</h3>\n'
        html += dbtable2html(relation)

    fd.write(html_document.format(body=html))



    
