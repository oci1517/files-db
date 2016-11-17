# -*- coding: utf-8 -*-

from dbutils import csv2dbtable

csvrecords = {}
csvfields = {}

csvfields['CLIENT'] = 'ClientID;Nom;Adresse;Ville;Canton;NoPostal'
csvrecords['CLIENT'] = '''
1;Archambault;2 Lindenstrasse;Zürich;ZH;8000
2;Au plaisir de Lire;10 route du Jura;Fribourg;FR;1700
3;Librairie du Nouveau Monde;35 rue des Acacias;Neuchâtel;NE;2000
4;Librairie La Liberté;1 avenue du Temple;Fribourg;FR;1700
5;Globe Trotteur;150 rue du Lac;Genève;GE;1200
6;Arts Lettres et Technique;20 Chaletweg;Basel;BS;4000
7;Camelot;7 Kramgasse;Luzern;LU;6000
8;Livres et Jardins;25 rue des Lilas;Bulle;FR;1630
9;Librairie du Centre;3 Place du Port;Nyon;GE;1260
10;Papyrus;40 rue de Carouge;Genève;GE;1200
11;Mes Lectures Jeunesse;12 rue des Sources;Genève;GE;1200
12;Univers Bandes Dessinées;52 avenue de la Gare;Lausanne;VD;1000
13;Librairie Ulysse;100 route de Meyrin;Genève;GE;1200
14;Librairie de l'Université;6 Haldenstrasse;Berne;BE;3000
15;Le Bouquiniste;1 place de Bel-Air;Genève;GE;1200
'''

csvfields['COMMANDE'] = 'CommandeID;Date;ClientID'
csvrecords['COMMANDE'] = '''
1001;2011-08-21;1
1002;2011-08-21;8
1003;2011-08-22;15
1004;2011-08-22;5
1005;2011-08-24;3
1006;2011-08-24;2
1007;2011-08-27;11
1008;2011-08-21;12
1009;2011-09-05;4
1010;2011-09-05;1

'''

csvfields['LIGNECOMMANDE'] = 'CommandeID;ProduitID;Quantite'
csvrecords['LIGNECOMMANDE'] = '''
1001;100;20
1001;300;5
1001;400;10
1002;300;2
1003;300;10
1004;300;30
1004;600;20
1004;800;20
1005;400;40
1006;400;10
1006;500;20
1006;700;20
1007;100;30
1007;200;20
1008;300;8
1008;800;30
1009;400;20
1009;700;30
1010;800;100
'''

csvfields['PRODUIT'] = 'ProduitID;Description;TypeReliure;PrixUnitaire'
csvrecords['PRODUIT'] = '''
100;Le guide des vins 2012;Cartonné;50
200;Dieux du stade;Cartonné;100
300;Rupture de contrat;Broché;10
400;Pars vite et reviens tard;Broché;12
500;Panique au collège;Broché;7
600;Marketing management;Spirales;120
700;L'art de la guerre;Cartonné;12
800;Excel pour le business et la finance;Spirales;75
900;10 ans de leçon de séduction;Cartonné;60
1000;Autant en emporte le vent;Cuir;150
'''

tables = ['CLIENT', 'COMMANDE', 'LIGNECOMMANDE', 'PRODUIT']

def DB():
    R = {}
    for t in tables:
        R[t] = csv2dbtable(t, csvfields[t], csvrecords[t])

    return R
