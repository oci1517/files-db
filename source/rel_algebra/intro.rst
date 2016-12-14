######################
Algèbre relationnelle
######################

..  ############### PROF UNIQUEMENT

..  only:: prof

    Remarques techniques et pédagogiques
    ====================================

    ..  admonition:: @prof Installation de SQLtable

        * Il faut installer l'extension SQLTable avec la commande  ::

            sudo pip install sphinxcontrib-sqltable

        * Il ne faut pas oublier d'ajouter l'extension dans le fichier :file:`conf.py`

..  ############### END PROF UNIQUEMENT


    Voici comment on peut connaître toutes les tables d'une base de données
    (et surtout comment on peut interroger une base de donneés SQLite) et
    afficher le résultat sous forme de table dans la documentation.
    ::

        ..  sqltable:: List of Users
            :connection_string: sqlite:///library.db
            :class: ocidbtable table-striped table-bordered

            SELECT tbl_name, sql from sqlite_master where type='table'

    Le répertoire racine correspond au dossier racine de la documentation (runestone)

    ..  sqltable:: List of Users
        :connection_string: sqlite:///library.db
        :class: ocidbtable table-striped table-bordered

        SELECT tbl_name, sql from sqlite_master where type='table'


Motivation
==========

Si le modèle relationnel a eu tant de succès au départ, c'est qu'il repose sur
des fondements mathématiques très solides. L'algèbre relationnelle permet de
formaliser la manière de poser des requêtes envers une base de données
relationnelles.

Le fait d'étudier un minimum d'algébre relationnelle va nous permettre de bien
comprendre comment fonctionne le modèle et comment un système de base de données
relationnelles va interroger les tables pour répondre à des questions précises.

Principes de base
=================

Dans l'algèbre relationnelle, on trouve essentiellement les ingrédients
suivants :

* des relations (ce sont en fait les tables contenant les données)
* des opérateurs relationnels opérant sur une ou deux relations (tables)

Les opérateurs relationnels
===========================

Les opérateurs relationnels sont des applications mathématiques qui prennent
en argument une ou deux relations et qui renvoient une nouvelle relation.

Nous verrons les opérateurs relationnels suivants

* Sélection (opérateur :math:`\sigma : R \longrightarrow R`)

* Projection (opérateur :math:`\pi : R \longrightarrow R`)

* Produit cartésien (opérateur :math:`\times : R \times R \longrightarrow R`)

..  Module Python d'algèbre relationnelle

Opérateur de sélection
----------------------

L'opérateur de sélection :math:`\sigma` prend une relation (table) et retourne
une autre relation dont certains tuples ont été enlevés. Cet opérateur filtre
donc les lignes de la table.


Exemple
~~~~~~~

.. sidebar:: Contenu des relations ``client`` et ``possession``
   :class: small

   ..  sqltable:: Contenu de la table ``client``
       :connection_string: sqlite:///bank.db
       :class: ocidbtable table-striped table-bordered

       select * from client


   ..  sqltable:: Table ``possession``
       :connection_string: sqlite:///bank.db
       :class: ocidbtable table-striped table-bordered

       select * from possession

   ..  only:: prof

       et que le contenu des autres tables est

       ..  sqltable:: Table ``compte``
           :connection_string: sqlite:///bank.db
           :class: ocidbtable table-striped table-bordered

           select * from compte

       ..  sqltable:: Table ``filiale``
           :connection_string: sqlite:///bank.db
           :class: ocidbtable table-striped table-bordered

           select * from filiale

       ..  sqltable:: Table ``possession``
           :connection_string: sqlite:///bank.db
           :class: ocidbtable table-striped table-bordered

           select * from possession

L'opération

..  math::

    \sigma_{\mathrm{client.no\_client > 3}}(\mathrm{client})

va retourner la table suivante qui ne contient que les enregistrements qui
satisfont à la condition :math:`\mathrm{client.no\_client > 3}` :

..  sqltable:: Résultat de la requête :math:`\sigma_{\mathrm{client.no\_client > 3}}(\mathrm{client})`
    :connection_string: sqlite:///bank.db
    :class: ocidbtable table-striped table-bordered

    select * from client where no_client > 3


Opérateur de projection
-----------------------

L'opérateur de projection :math:`\pi` prend une table en argument et ne garde
que les colonnes mentionnées.

Exemple
~~~~~~~

Si l'on projète la table ``client`` sur les colonnes ``client.nom`` avec
l'opération

..  math::

    \pi_{\mathrm{client.nom, client.prenom}}(\mathrm{client})

on obtiendrait la table ``client`` sans les colonnes autres que ``client.nom``
et ``client.prenom`` :

..  sqltable:: Résultat de la requête :math:`\pi_{\mathrm{client.nom, client.prenom}}(\mathrm{client})`
    :connection_string: sqlite:///bank.db
    :class: ocidbtable table-striped table-bordered

    select client.nom, client.prenom from client

Combinaison d'opérations
------------------------

Puisque les opérateurs relationnels sont définis sur les ensembles de
relations et retournent des relations, il est possible de les composer, comme
on composer des fonctions :math:`f : \mathbb{R} \longrightarrow \mathbb{R}` en
mathématiques.

Exemple
~~~~~~~

On peut combiner par exemple une sélection et une projection pour obtenir le
nom et le prénom de tous les clients tels que ``client_no > 3`` avec la
requête :

..  math::

    \pi_{\mathrm{client.nom, client.prenom}} (\sigma_{\mathrm{client.no\_client > 3}} (\mathrm{client}))

qui donnera le résultat

..  sqltable:: Résultat de la requête :math:`\pi_{\mathrm{client.nom, client.prenom}} (\sigma_{\mathrm{client.no\_client > 3}} (\mathrm{client}))`
    :connection_string: sqlite:///bank.db
    :class: ocidbtable table-striped table-bordered

    select client.nom, client.prenom from client where client.no_client > 3

..  admonition:: Remarque

    On n'aurait pas pu effectuer la projection en premier, car la sélection
    n'aurait plus pu filtrer les lignes en fonction de la colonne
    ``client.no_clien``. La requête suivante n'est donc pas correcte :

    ..  math::

        \sigma_{\mathrm{client.no\_client > 3}} (\pi_{\mathrm{client.nom, client.prenom}} (\mathrm{client}))

Opérateur de produit cartésien
------------------------------

Le produit cartésien de deux tables est une table souvent gigantesque dans
laquelle on combine chaque ligne de la première table avec chaque ligne de la
deuxième table.


Exemple
~~~~~~~

Le produit cartésien de la table ``client`` avec la table ``possession``, noté

..  math::

    \mathrm{client} \times \mathrm{possession}



donne le résultat de la table suivante :

..  sqltable:: Résultat du produit cartésien :math:`\mathrm{client} \times \mathrm{compte}`
    :connection_string: sqlite:///bank.db
    :class: ocidbtable table-striped table-bordered

    select * from client, possession

En combinant avec un produit cartésien et une sélection, on peut ne garder du
gigantesque produit cartésien que les lignes qui nous intéressent,
caractérisées par la condition
::
    possession.no_client = client.no_client and client.nom = 'Turing'

pour déterminer tous les comptes que possède le client avec ``client.nom =
'Turing'`` :

..  sqltable:: Résultat de la requête :math:`\sigma_{\mathrm{possession.no\_client = client.no\_client \wedge client.nom = 'Turing'}} (\mathrm{client} \times \mathrm{possession})`
    :connection_string: sqlite:///bank.db
    :class: ocidbtable table-striped table-bordered

    select * from possession, client where possession.no_client = client.no_client and client.nom = 'Turing'

Avec une projection sur la colonne ``possession.no_compte``, on ne peut garder
que le numéro de compte :

..  sqltable:: Résultat de la requête :math:`\pi_{\mathrm{possession.no\_compte}} \left(\sigma_{\mathrm{possession.no\_client = client.no\_client \wedge client.nom = 'Turing'}} (\mathrm{client} \times \mathrm{possession}) \right)`
    :connection_string: sqlite:///bank.db
    :class: ocidbtable table-striped table-bordered

    select possession.no_compte
    from possession, client
    where possession.no_client = client.no_client and client.nom = 'Turing'
