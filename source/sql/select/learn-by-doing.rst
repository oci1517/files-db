###################################
Instruction ``SELECT`` : exemples commentés
###################################

..  header:: salut

Introduction
============

Les requêtes détaillées dans cette section sont effectuées sur la base de
données SQLite ``library.db`` (voir :ref:`sec-databases-show-library`)

..  sql-connection-config:: sqlite:///library.db

Exemples simples
================

..  butreq::

    Sélectionner toutes les colonnes sur tous les clients (afficher
    l'intégralité de la table ``client``)

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/5

    SELECT *
    FROM client

..  butreq::
    
    Sélectionner le nom et l’adresse de tous les clients

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/6

    SELECT  
        nom, adresse
    FROM
        client    

..  butreq::

    Montrer l'utilisation d’expressions mathématiques parmi les colonnes de la
    table résultat.

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/7

    SELECT 
        description,
        prix_unitaire,
        prix_unitaire + (prix_unitaire + 2.4 / 100) + 6
    FROM
        produit


Fonctions et opérations d’agrégation
====================================

..  butreq::

    Liste des prix de tous les produits

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/9

    SELECT
        prix_unitaire
    FROM
        produit

..  butreq::

    Déterminer

    *   le nombre de produits
    *   la somme des prix de tous les produits
    *   le prix moyen des produits

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/10

    SELECT
        COUNT(prix_unitaire ) AS "Nombre de produits",
        SUM(prix_unitaire) AS "Somme des prix",
        AVG(prix_unitaire) AS "Prix unitaire moyen"
    FROM
        produit


..  sql::
    :fiddle: http://sqlfiddle.com/#!7/a7459/12

    SELECT
        description,
        AVG(prix_unitaire) AS "Prix unitaire moyen"
    FROM
        produit

..  admonition:: Attention

    Ceci produit une erreur SQL. Attention, cette requête
    fonctionne sous SQLite3 mais cela n’est pas conforme au standard SQL.

..  butreq::

    Nombre de clients domiciliés dans chaque canton

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/13

    SELECT
        client.canton,
        COUNT(client.client_id)
    FROM
        client
    GROUP BY
        client.canton

..  butreq::

    Déterminer le nombre de clients domiciliés dans le canton de Genève

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/14

    SELECT
        client.canton, COUNT(client.client_id)
    FROM
        client
    WHERE
        client.canton = 'GE'
    GROUP BY
        client.canton

..  butreq::

    Combien y a-t-il de titres (livres) différents dans la commande No. 1004 ?

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/16

    SELECT 
        COUNT(*) AS "Nombre de titres"
    FROM
        ligne_commande
    WHERE
        ligne_commande.commande.commande_id = 1004


..  only:: prof

    ..  #################################################################
    ######################
    ######################
    ######################
    ######################
    ######################
    ######################

    Fonctions concernant les dates
    ==============================

    ..  admonition:: À réviser avec la syntaxe des dates de SQLite

        ..  admonition:: Page de référence SQLite sur les fonctions de gestion des dates et de l'heure

            http://www.sqlite.org/cvstrac/wiki/wiki?p=DateAndTimeFunctions
        
        
        ..  admonition:: à revoir

            ..  sql:: Liste des commandes avec leur âge

                SELECT
                    commande.commande.commande_id,
                    commande.date,
                    DateDiff('d', commande.date, NOW())
                FROM
                    commande


        ..  sql:: Sélectionner les commandes qui datent de plus de 2300 jours

            SELECT
                commande.commande.commande_id,
                commande.date
            FROM
                commande
            WHERE
                DateDiff('d', date, NOW()) > 2300
        
        ..  sql::   Commandes de livres placées après le 24.08.2004 dans la table commande.

            SELECT
                commande.commande.commande_id, commande.date
            FROM
                commande
            WHERE   commande.date > date('2004-08-24')
     
    ..  #################################################################
    ######################
    ######################
    ######################
    ######################
    ######################
    ######################

Tri des résultats
=================

..  butreq::

    Liste des clients triés par nom

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/18
    
    SELECT
        client.nom,
        client.canton 
    FROM
        client
    ORDER BY (client.nom) ASC   -- tri croissant


..  butreq::

    Liste des clients triés par nom dans l’ordre décroissant

..  sql::
    :fiddle: http://sqlfiddle.com/#!7/a7459/19

    SELECT
        client.nom,
        client.canton 
    FROM    
        client
    ORDER BY (client.nom) DESC  -- tri décroissant d'après le nom du client


..  butreq::    
    
    Liste des clients triés par cantons puis par noms    

..  sql:: 
    :fiddle: http://sqlfiddle.com/#!7/a7459/24

    SELECT
        client.nom,
        client.canton
    FROM
        client
    ORDER BY client.canton, client.nom  -- ordre important !!

..  butreq::

    Idem mais en triant les cantons dans l’ordre décroissant

..  sql::
    :fiddle: http://sqlfiddle.com/#!7/a7459/25

    SELECT
        client.nom,
        client.canton
    FROM
        client
    ORDER BY client.canton DESC, client.nom 

Opérateurs logiques
===================

..  butreq::

    Indiquer le titre, le type de reliure et le prix unitaire

    *   de tous les livres brochés (quel que soit leur prix)
    *   et des livres cartonnés dont le prix est supérieur à 50 CHF.

..  sql::
    http://sqlfiddle.com/#!7/a7459/31
    
    SELECT
        produit.description,
        produit.reliure,
        produit.prix_unitaire 
    FROM 
        produit
    WHERE
        produit.reliure = 'Broché'
        OR
            (produit.reliure = 'Cartonné'
            AND produit.prix_unitaire > 50)

..  butreq::

    Indiquer le titre, le type de reliure et le prix unitaire

    *   de tous les livres brochés ou cartonnés
    *   dont le prix est supérieur à 50 CHF.

..  sql::

    SELECT 
        produit.description,
        produit.reliure,
        produit.prix_unitaire 
    FROM
        produit
    WHERE
        (produit.reliure = 'Broché'
        OR produit.reliure = 'Cartonné')
        AND produit.prix_unitaire > 50

..  butreq::        

    Trouver les livres dont le prix unitaire est compris entre 50 francs et
    100 francs, bornes comprises.

..  sql::

    SELECT
        produit.description,
        produit.prix_unitaire 
    FROM
        produit
    WHERE   
        produit.prix_unitaire >= 50
        AND produit.prix_unitaire <= 100

ou bien

..  sql::

    SELECT
        produit.description,
        produit.prix_unitaire 
    FROM
        produit
    WHERE   
        produit.prix_unitaire BETWEEN 50 AND 100

Renommer les colonnes du résultat
=================================    

..  butreq::

    Sélectionner le nom et l’adresse du client ‘Globe Trotteur’

..  sql::

    SELECT
        client.nom,
        client.adresse
    FROM
        client
    WHERE
        client.nom = 'Globe Trotteur'

..  butreq::

    Effectuer la même requête, mais en renommant es colonnes par ``Nom du client``
    et ``Adresse du client``

..  sql::

    SELECT
        client.nom AS 'Nom du client',
        client.adresse AS 'Adresse du client'
    FROM
        client
    WHERE
        client.nom = 'Globe Trotteur'    


Compter le nombre de lignes du résultata
========================================

..  butreq:: 
    
    Déterminer le nombre de clients

..  sql::

    SELECT COUNT(*) AS "Nombre de clients"
    FROM client

..  admonition:: Explication

    Dans cette requête, on compte le nombre de lignes qui apparaitraient dans
    le résultat de la requête SQL suivante :

    ..  code-block:: sql

        SELECT * FROM client

..  butreq::

    Nombre de commandes

..  sql::
    SELECT
        COUNT(*) AS "Nombre de commandes"
    FROM
        commande        

Produits cartésiens et jointures de tables
==========================================

..  butreq::

    *   Produit cartésien entre la table ``client`` et ``commande``

    *   **Attention** : Le résultat est tronqué ! En réalité, la table comporte 150 lignes !!!

    *   Chaque enregistrement de la table ``commande`` est combiné avec toutes
        les lignes de la table ``client``

..  sql::
    :fiddle: http://sqlfiddle.com/#!5/a7459/1

    SELECT
        commande.*, client.*
    FROM
        commande, client
    LIMIT 20

..  admonition:: Remarque
 
    La plupart des lignes de ce produit cartésien ne servent à rien car les
    champs client_id des deux tables ne correspondent pas dans la plupart des
    cas.

..  butreq::

    Taille du produit cartésien entre la table ``client`` et ``commande``.

..  sql::

    SELECT  count(*) 
    FROM    client, commande

..  admonition:: Remarque

    La taile du produit cartésien entre les tables ``client`` et ``commande``
    vaut ::

        size(client) * size(commande)) = 10 * 15 = 150

    où ``size(table)`` indique la taille de la table ``table``.

..  butreq::

    Liste de toutes les commandes avec le client concerné

Jointure de tables
------------------

Pour effectuer correctement une jointure de tables et ne garder que les lignes
pour lesquelles la partie ``client`` est en relation avec la partie
``commande``, on effectue une sélection en ajoutant une condition du type ::

    table1.cle_primaire = table2.cle_etrangere

..  sql::

    SELECT
        commande.commande_id,
        client.nom
    FROM
        client, commande
    WHERE
        --- condition de jointure des tables
        commande.client_id = client.client_id


..  butreq::

    Toutes les commandes du client ``Archambault``

..  req::

    SELECT
        commande.commande_id,
        client.nom
    FROM
        client, commande
    WHERE
        commande.client_id = client.client_id
        AND client.nom = 'Archambault'

 
Autres spécialités de l’instruction SELECT
==========================================

..  butreq::

    Liste des cantons où notre grossiste possède plus qu’un client

..  sql::

    SELECT
        client.canton,
        COUNT(client.canton) AS [Nombre de clients]
    FROM
        client
    GROUP BY
        client.canton 
    HAVING COUNT(client.canton) > 1

..  butreq::

    *   Liste de tous les clients établis dans les cantons romands en indiquant
        leur nom, ville et canton.

    *   Chaque canton est est représenté par deux
        lettres dans la colonne ``client.canton`` de la table ``client``.

..  sql::        

    SELECT
        client.nom,
        client.ville,
        client.canton,
    FROM
        client
    WHERE
        client.canton IN ('FR', 'GE', 'NE', 'VD')

..  butreq::
    
    Cette requête produit une erreur : le champ ``client_id`` existe dans
    plusieurs tables et il faut les distinguer

..  sql::

    SELECT
        client_id,
        commande.commande_id,
        client.nom
    FROM
        client, commande
    WHERE
        commande.client_id = client.client_id

..  butreq::

    Correction de la requête précédente en spécifiant la table avec
    ``client.client_id`` pour lever l’ambiguité.

..  sql::

    SELECT
        client.client_id,
        commande.commande_id,
        client.nom
    FROM
        client, commande
    WHERE
        commande.client_id = client.client_id

