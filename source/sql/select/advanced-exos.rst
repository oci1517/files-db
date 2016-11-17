###############################
``SELECT`` : exercices avancés
###############################

Exercice 1
==========

..  sql-connection-config:: sqlite:///library.db

..  admonition:: Base de données concernée

    Les requêtes de cet exercice concernent la base de données décrite en détails dans
    :ref:`sec-databases-show-library`.

#)  La requête retourne le nom et l'adresse des clients romands dont le nom commence par une voyelle

    ..  sql::
        :no-query:
        :corrige:

        SELECT 
            client.nom,
            client.adresse
        FROM client
        WHERE
            client.canton IN ('VS', 'FR', 'VD', 'GE', 'JU', 'NE')
            AND client.nom LIKE 'A%'
            OR client.nom LIKE 'E%'
            OR client.nom LIKE 'É%'
            OR client.nom LIKE 'È%'
            OR client.nom LIKE 'Ê%'
            OR client.nom LIKE 'I%'
            OR client.nom LIKE 'O%'
            OR client.nom LIKE 'U%'
            OR client.nom LIKE 'Y%'


#)  La requête retourne le nombre de clients genevois

    ..  sql::
        :no-query:
        :corrige:

        SELECT 
            COUNT(*) AS [Nombre de clients genevois]
        FROM client
        WHERE
            client.canton = 'GE'

#)  La requête retourne le nombre de produits proposés par le grossiste, 
    la somme du prix de tous les produits ainsi que
    leur prix unitaire moyen

    ..  sql::
        :no-query:
        :corrige:

        SELECT 
            COUNT(*) AS [Nombre de produits proposés],
            SUM(produit.prix_unitaire) AS [Somme des prix de tous les produits],
            AVG(produit.prix_unitaire) AS [Moyenne des prix de tous les produits],
            MAX(produit.prix_unitaire) AS [Produit ayant le plus haut prix],
            MIN(produit.prix_unitaire) AS [Produit ayant le plus bas prix]
        FROM produit               

#)  La requête retourne le prix unitaire moyen des produits cartonnés

    ..  sql::
        :no-query:
        :corrige:

        SELECT 
            AVG(produit.prix_unitaire) AS [Moyenne des prix de tous les produits]
        FROM produit
        WHERE
            produit.reliure LIKE '%Cartonné%'

#)  La requête retourne la description des produits cartonnés dont le prix unitaire 
    est inférieur ou égal à 80 francs

    ..  sql::
        :no-query:
        :corrige:

        SELECT 
            produit.description AS [Produit dont le prix est inférieur à 80 CHF]
        FROM
            produit
        WHERE
            produit.reliure LIKE '%Cartonné%'
            AND produit.prix_unitaire < 80


#)  La requête retourne le nombre de clients ayant passé une commande auprès du fournisseur

    ..  sql::
        :no-query:
        :corrige:

        SELECT 
          COUNT(*) AS [Nombre de clients distincts ayant passé une commande]
        FROM (
          SELECT DISTINCT
              client.client_id
          FROM
              client, commande
          WHERE
              client.client_id = commande.client_id
         )

    ..  only:: corrige

        ..  admonition:: Remarque

            Dans cette requête, on utilise une requête imbriquée. En pratique,
            on peut placer une requête ``SELECT`` partout où on peut placer
            une table.

            Ici, on place une requête ``SELECT`` à la place de la table à
            partir de laquelle 

#)  La requête retourne le nombre de titres (livres) différents présents dans la commande 1004

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            COUNT(*) AS [Nombre de titres différents dans la commande 1004]
        FROM
            ligne_commande
        WHERE
            ligne_commande.commande_id = 1004

#)  La requête retourne le numéro de toutes les commandes passées après le 31 août 2011
    
    ..  sql::
        :no-query:
        :corrige:

        SELECT
            commande.commande_id AS [Numéro de commande],
            commande.date AS [Date de la commande]
        FROM
            commande
        WHERE
            commande.date > date('2011-08-31')

#)  La requête retourne le numéro de toutes les commandes
    datant de plus de 168 jours à compter du 8 février 2012.

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            commande.commande_id AS [Numéro de commande],
            commande.date AS [Date de la commande]
        FROM
            commande
        WHERE
            julianday('2012-02-08') - julianday(commande.date) > 168

#)  Liste des numéros de commandes avec leur âge respectif, l'âge d'une commande étant le nombre
    de jours qui se sont écoulés depuis la commande jusqu'à aujourd'hui.

    ..  tip::

        L'appel ``date('now')`` retourne la date d'aujourd'hui

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            commande.commande_id AS [Numéro de commande],
            julianday(date('now')) - julianday(commande.date) AS [Âge de la commande]
        FROM
            commande

    ..  only:: corrige    

        Voici une version alternative qui affiche l'âge en nombres entiers. Remarquez l'utilisation de
        l'opérateur ``CAST (expression) AS type`` pour convertir l'expression de type ``REAL`` en 
        un type ``INTEGER``.

        ..  sql::

            SELECT
                commande.commande_id AS [Numéro de commande],
                CAST (julianday(date('now')) - julianday(commande.date) AS INTEGER) AS [Âge de la commande],
                'jours' AS [Unité]
            FROM
                commande

Exercice 2 (Fonctions d'aggrégation et clause ``GROUP BY``)
===========================================================

..  prof::

    ..  admonition:: @prof (Objectifs de l'exercice)

        Cet exercice entraîne surtout les fonctions d'aggrégations ainsi que
        l'utilisation de la clause ``GROUP BY``

..  sql-connection-config:: sqlite:///library.db

..  admonition:: Base de données concernée

    Les requêtes de cet exercice concernent la base de données décrite en détails dans
    :ref:`sec-databases-show-library`.            


#)  Le montant total de la commande '1001'

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            SUM(quantite * prix_unitaire) AS [Montant total de la commande]
        FROM
            ligne_commande, produit
        WHERE
            ligne_commande.produit_id = produit.produit_id
            AND ligne_commande.commande_id = 1001

#)  Liste des commandes indiquant le montant total de chaque commande

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            ligne_commande.commande_id AS [Numéro de commande],
            SUM(quantite * prix_unitaire) AS [Montant total de la commande]
        FROM
            ligne_commande, produit
        WHERE
            ligne_commande.produit_id = produit.produit_id
        GROUP BY ligne_commande.commande_id        


#)  Liste des commandes passées par le client 'Archambault'. On veut connaitre
    pour chaque commande le montant total de la commande

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            ligne_commande.commande_id AS [Numéro de commande],
            SUM(quantite * prix_unitaire) AS [Montant total de la commande]
        FROM
            ligne_commande, produit, commande, client
        WHERE
            ligne_commande.produit_id = produit.produit_id
            AND commande.client_id = client.client_id
            AND ligne_commande.commande_id = commande.commande_id
            AND client.nom = 'Archambault'
        GROUP BY ligne_commande.commande_id


#)  Le montant total de l'ensembles des commandes passées par le client 'Archambault'.

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            SUM(ligne_commande.quantite * produit.prix_unitaire) AS [Montant total des commandes de Archambault]
        FROM
            ligne_commande, produit, commande, client
        WHERE
            ligne_commande.produit_id = produit.produit_id
            AND commande.client_id = client.client_id
            AND ligne_commande.commande_id = commande.commande_id
            AND client.nom = 'Archambault'  


Exercice 3 : clauses ``HAVING`` / ``GROUP BY`` / ``ORDER BY``
============================================================

..  prof::

    ..  admonition:: @prof (Objectifs de l'exercice)

        Cet exercice entraîne surtout les fonctions d'aggrégations ainsi que
        l'utilisation des clauses ``GROUP BY`` et ``HAVING``

..  todo::

    Rajouter encore au moins deux requêtes exigeant la clause ``HAVING``

..  todo::

    Mettre un exercice dont la clause ``HAVING`` contient plusieurs fonctions
    d'aggrégation et éventuellement une fonction mathématique ou une
    expression logique composée.

..  sql-connection-config:: sqlite:///library.db

..  admonition:: Base de données concernée

    Les requêtes de cet exercice concernent la base de données décrite en détails dans
    :ref:`sec-databases-show-library`.

#)  Numéro des commandes dont le total est supérieur à 4000 CHF. Pour chaque commande, on 
    veut également connaître le montant de la commande.

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            ligne_commande.commande_id AS [Numéro de commande],
            SUM(ligne_commande.quantite * produit.prix_unitaire) AS [Montant total de la commande]
        FROM
            ligne_commande, produit
        WHERE
            ligne_commande.produit_id = produit.produit_id
        GROUP BY 
            ligne_commande.commande_id
        HAVING 
            SUM(ligne_commande.quantite * produit.prix_unitaire) > 4000

#)  La requête retourne la liste des livres cartonnés classée du plus au moins cher

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            description AS [Nom du produit],
            prix_unitaire AS [Prix unitaire]
        FROM    
            produit
        WHERE 
            reliure = 'Cartonné'
        ORDER BY prix_unitaire DESC

#)  La requête retourne la liste du nombre de clients que compte chaque ville
    suisse inscrite dans la base de données

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            ville AS [Ville],
            COUNT(client_id) AS [Nombre de clients]
        FROM    
            client
        GROUP BY
            ville
        ORDER BY [Nombre de clients]

#)  La requête retourne la liste du nombre de clients que compte chaque ville
    suisse inscrite dans la base de données. Les résultats sont triés selon
    l'ordre croissant du nombre de clients.

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            ville AS [Ville],
            COUNT(client_id) AS [Nombre de clients]
        FROM    
            client
        GROUP BY
            ville
        ORDER BY [Nombre de clients]        


#)  La requête retourne la liste décroissante du nombre de produits pour chaque
    type de reliure proposé

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            reliure AS [Type de reliure]   ,
            COUNT(produit_id) AS [Nombre de produits]
        FROM
            produit
        GROUP BY
            reliure
        ORDER BY [Nombre de produits] DESC

#)  La requête retourne la liste décroissante du nombre d'exemplaires de chaque
    produit commandé auprès du fournisseur pour autant que ce nombre soit
    supérieur ou égal à 50.

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            produit.description AS [Nom du produit],
            SUM(ligne_commande.quantite) AS [Quantité d''exemplaires commandés]
        FROM
            ligne_commande, produit
        WHERE
            ligne_commande.produit_id = produit.produit_id
        GROUP BY 
            ligne_commande.produit_id
        HAVING
            SUM(ligne_commande.quantite) >= 50

#)  La requête retourne la liste des prix unitaires moyens des produits par type
    de reliure proposé pour autant que ces prix unitaires moyens n'excéde pas 60
    francs. 

    *   On ne considère que les produits cartonnés, brochés ou avec spirales

    *   Le résultat doit être affiché dans l'ordre alphabétique des types de
        reliure.

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            reliure AS [Type de reliure],
            AVG(prix_unitaire) AS [Prix moyen des produits]
        FROM
            produit
        WHERE
            reliure IN ('Cartonné', 'Broché', 'Spirales')
        GROUP BY 
            reliure
        HAVING
            AVG(prix_unitaire) <= 60
        ORDER BY reliure ASC 


..  todo::

    Exercice de synthèse faisant intervenir

    *   pattern matching avec l'opérateur ``LIKE``

    *   GROUP BY / HAVING

    *   ORDER BY


Exercice 4 : exercie d'entrainement
===================================

..  sql-connection-config:: sqlite:///library.db

..  admonition:: Base de données concernée

    Les requêtes de cet exercice concernent la base de données décrite en détails dans
    :ref:`sec-databases-show-library`.


#)  La requête retourne la liste des clients ayant passé une commande après le 31 août 2011

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            client.nom AS [Nom du client],
            commande.date AS [Date de la commande]
        FROM
            client, commande
        WHERE
            commande.client_id = client.client_id
            AND commande.date > date('2011-08-31')

#)  La requête retourne le nombre de clients ayant déjà passé une commande
    auprès du fournisseur.

    ..  sql::  
        :no-query:
        :corrige:


        SELECT
            COUNT(DISTINCT commande.client_id)
                AS [Nombre de clients ayant déjà effectué une commande]
        FROM
            commande

    ..  admonition:: Commentaire

        Remarquez la présence du mot ``DISTINCT`` devant la colonne à compter
        avec la fonction ``COUNT()``. Ceci permet de ne pas compter à double
        les clients ayant passé plusieurs commandes.

        
#)  La requête retourne la liste des produits commandés par le client 'Archambault'
    en indiquant pour chaque produit le nombre d'exemplaires commandés.

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            produit.description AS [Nom du produit],
            SUM(ligne_commande.quantite) AS [Nombre d'exemplaires commandés]
        FROM
            ligne_commande, produit, client, commande
        WHERE
            ligne_commande.produit_id = produit.produit_id
            AND commande.commande_id = ligne_commande.commande_id
            AND client.client_id = commande.client_id
            AND client.nom LIKE 'Archambault'
        GROUP BY
            produit.description

#)  La requête retourne la liste décroissante des clients ayant commandé le plus
    d'exemplaires de produits en indiquant pour chaque client le nombre total
    d'exemplaires commandés.

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            client.nom AS [Client],
            SUM(ligne_commande.quantite) AS [Nombre d'exemplaires commandés]
        FROM
            ligne_commande, produit, client, commande
        WHERE
            ligne_commande.produit_id = produit.produit_id
            AND commande.commande_id = ligne_commande.commande_id
            AND client.client_id = commande.client_id
        GROUP BY
            commande.client_id
        ORDER BY 
            [Nombre d'exemplaires commandés] DESC

#)  La requête retourne la liste décroissante des produits les plus commandés
    en indiquant pour chacun le nombre d'exemplaires commandés.

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            produit.description AS [Produit],
            SUM(ligne_commande.quantite) AS [Nombre d'exemplaires commandés]
        FROM
            ligne_commande, produit
        WHERE
            ligne_commande.produit_id = produit.produit_id
        GROUP BY
            ligne_commande.produit_id
        ORDER BY 
            [Nombre d'exemplaires commandés] DESC


Exercice 5 : requêtes imbriquées
================================

..  admonition:: Consigne

    Dans cet exercice, utilisez des requêtes imbriquées

#)  La requête retourne la liste des clients n'ayant jamais passé de
    commande auprès du fournisseur.

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            client.nom AS [Nom du client]
        FROM
            client
        WHERE
            client_id NOT IN (
                SELECT DISTINCT client_id FROM commande
            )


#)  La requête retourne la liste des clients ayant passé une commande avec un
    nombre total d'exemplaires commandés supérieur aux nombre d'exemplaires
    commandés dans la commande 1006.

    ..  sql::  
        :no-query:
        :corrige:

        SELECT
            client.nom AS [Client],
            commande.commande_id AS [Numéro de la commande],
            SUM(quantite) AS [Nombre d'exemplaires dans la commande]
        FROM
            client, commande, ligne_commande
        WHERE
            client.client_id = commande.client_id
            AND commande.commande_id = ligne_commande.commande_id
        GROUP BY
            commande.commande_id
        HAVING
            [Nombre d'exemplaires dans la commande] > (
                SELECT SUM(quantite) as [quantite]
                FROM ligne_commande
                WHERE ligne_command e.commande_id = 1006
            )