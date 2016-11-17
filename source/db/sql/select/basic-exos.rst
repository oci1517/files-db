###############################
``SELECT`` : exercices basiques
###############################

Exercice 1
==========

..  sql-connection-config:: sqlite:///library.db

..  admonition:: Base de données concernée

    Les requêtes de cet exercice concernent la base de données décrite en détails dans
    :ref:`sec-databases-show-library`.

Écrivez une requête SQL permettant d'afficher les informations demandées

#)  Le nom et l'adresse du client 'Globe Trotteur'

    ..  sql::
        :no-query:
        :corrige:

        SELECT client.nom, client.adresse
        FROM client
        WHERE
            client.nom = 'Globe Trotteur'

#)  Le nom et l'adresse des clients habitant le canton de Fribourg

    ..  sql::
        :no-query:
        :corrige:

        SELECT client.nom, client.adresse
        FROM client
        WHERE
            client.canton = 'FR'

#)  Toutes les informations concernant les produits dont le 
    prix est supérieur à 50 CHF

    ..  sql::
        :no-query:
        :corrige:

        SELECT *
        FROM produit
        WHERE produit.prix_unitaire > 50

#)  Le nom des produits qui ont été commandés par le client 'Archambault'. 
    Pour chaque produit, on veut connaître le nombre d'exemplaires commandés.

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            produit.description AS 'Nom du produit',
            ligne_commande.quantite AS 'Quantité commandée'
        FROM
            client, commande, ligne_commande, produit
        WHERE
            client.client_id = commande.client_id
            AND produit.produit_id = ligne_commande.produit_id
            AND commande.commande_id = ligne_commande.commande_id
            AND client.nom = 'Archambault'

#)  Le nom des produits qui ont été commandés par le client 'Archambault'. 
    Pour chaque produit, on veut connaître le montant déboursé pour l'ensemble des exemplaires de ce produit.

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            produit.description AS 'Nom du produit',
            ligne_commande.quantite * produit.prix_unitaire AS [Montant total pour l'article]
        FROM
            client, commande, ligne_commande, produit
        WHERE
            client.client_id = commande.client_id
            AND produit.produit_id = ligne_commande.produit_id
            AND commande.commande_id = ligne_commande.commande_id
            AND client.nom = 'Archambault'    


#)  Nom et type de reliure des produits qui sont cartonnés ou brochés. 
    Utiliser les opérateurs logiques dans la condition de sélection.

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            produit.description AS 'Nom du produit',
            produit.reliure AS 'Type de reliure'
        FROM
            produit
        WHERE
            produit.reliure = 'Broché'
            OR produit.reliure = 'Cartonné'


Exercice 2 (Opérateur 'LIKE')
===============================

..  sql-connection-config:: sqlite:///library.db

..  admonition:: Base de données concernée

    Les requêtes de cet exercice concernent la base de données décrite en détails dans
    :ref:`sec-databases-show-library`.

#)  Décrire en français ce que fait l'opérateur 'LIKE' utilisé
    dans la requête suivante en consultant la documentation de la 
    requête 'SELECT'. Tester la requête dans SQLFiddle.

    ..  sql::
        :no-output:
        :corrige:

        SELECT
            client.nom
        FROM
            client
        WHERE
            client.nom LIKE 'Librairie%' 

#)  Écrire une requête qui permet de connaitre le nom de tous les
    clients dont le nom commence par le caractère 'A'.

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            client.nom AS 'Clients dont le nom commence par A'
        FROM
            client
        WHERE
            client.nom LIKE 'A%'

#)  Écrire une requête permettant de trouver tous les produits dont
    la description contient le mot 'de'

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            produit.description AS [Produits contenant le mot de]
        FROM
            produit
        WHERE
            produit.description LIKE '% de %'


Exercice 3 (Opérateur 'IN')
=============================

..  sql-connection-config:: sqlite:///library.db

..  admonition:: Base de données concernée

    Les requêtes de cet exercice concernent la base de données décrite en détails dans
    :ref:`sec-databases-show-library`.

#)  Décrire en français ce que fait l'opérateur 'IN' utilisé
    dans la requête suivante en consultant la documentation de la 
    requête 'SELECT'. Tester la requête dans SQLFiddle.

    ..  admonition:: Document utile

        * http://www.w3schools.com/sql/sql_in.asp

    ..  sql::
        :no-output:
        :corrige:

        SELECT
            produit.description, produit.reliure
        FROM
            produit
        WHERE
            produit.reliure IN ('Broché', 'Cartonné')

#)  Écrire une requête qui renvoie le nom, l'adresse et le canton des clients
    domicilés dans un canton romand.

    ..  tip::
    
        Les cantons romands sont 'GE', 'VD', 'NE', 'FR', 'VS', 'JU'.

    ..  sql::
        :no-query:
        :corrige:

        SELECT
            client.nom AS [Nom du client],
            client.adresse AS [Adresse],
            client.canton AS [Canton]
        FROM
            client
        WHERE
            client.canton IN ('GE', 'VD', 'NE', 'FR', 'VS', 'JU')
