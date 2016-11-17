# -*- coding: utf-8 -*-

from collections import namedtuple, OrderedDict

from dbutils import dbtable2html

####################################
## Définition de la base de données relationnelle



def relname(rec):
    return rec.__class__.__name__

def relfields(rel, fields):
    return [rel + '_' + f for f in fields]

# Affichage de la base de données
def selection(relation, condition):
    result_R = []
    
    for r in relation:
        if eval(condition) is True:
            result_R.append(r)
    return result_R



def projection(relation, cols):
    result_R = []

    for record in relation:
        NewRecord = namedtuple(record.__class__.__name__, cols)

        recordDict = record._asdict()
        newRecordData = []
        for col in cols:
            newRecordData.append(recordDict[col])
            
        newRecord = NewRecord._make(newRecordData)
        result_R.append(newRecord)

    return result_R

def cartprod(rel1, rel2):
    result_R = []
                               
    for r1 in rel1:
        for r2 in rel2:
            ProductRecord = namedtuple('{}_{}'.format(relname(r1), relname(r2)),
                               relfields(relname(r1), r1._fields) +
                               relfields(relname(r2), r2._fields))
            
            result_R.append(ProductRecord._make(r1 + r2))

    return result_R

    

