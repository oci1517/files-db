##########################################################################
Interrogation de la base de données, les bases de l'instruction ``SELECT``
##########################################################################

Les bases de données relationelles sont interrogées à l'aide de l'instruction
SQL ``SELECT``. Cette dernière permet de réaliser les opérations de l'algèbre
relationnelle, à savoir 

* Le produit cartésien
* La sélection
* La projection

ainsi que bien d'autres encore.

..  only:: latex

    ..  admonition:: Présentation vidéo

        * Lien : http://youtu.be/mdDdd7vTJZ4

..  only:: html

    Vidéo de présentation
    =====================

    ..  youtube:: mdDdd7vTJZ4

    ..  admonition:: Errata

        Il y a une erreur dans la vidéo dans la partie traitant de l'opération
        de sélection. Il est mentionné qu'il faut mettre les nombres entiers
        entre apostrophes dans la requête

        ..  code-block:: sql

            SELECT *
            FROM client
            WHERE client.no_client > '3'

        Cette requête fonctionne dans SQLite de même que dans certains autres
        SGBDR, mais ce n'est pas la syntaxe défnie par le standard SQL. La
        syntaxe correcte consiste à mettre uniquement les chaines de
        caractères entre apostrophes, mais pas les nombres entiers :

        **Code corrigé**

        ..  code-block:: sql

            SELECT *
            FROM client
            WHERE
                client.no_client > 3
                OR client.nom = 'Honegger'

    ..  admonition:: Timing de la vidéo

        * ``00:10`` : introduction / objectifs
        * ``01:34`` : Affichage d'une table
        * ``03:54`` : Opération de projection
        * ``06:25`` : Présentation de la clause ``AS`` permettant de renommer les colonnes
        * ``07:37`` : Opération de sélection
        * ``11:50`` : Opération de produit cartésien
        * ``14:18`` : Utilisation de la clause ``AS`` pour renommer les tables à l'intérieur de la clause ``FROM``
        * ``15:32`` : Combinaison des opérations de sélection, projection et produit cartésien 
          (exemple réel : Liste des numéros de comptes de Arthur Honegger)
        * ``19:30`` : Résumé
        * ``20:27`` : Aperçu des autres possibilités de la fonction ``SELECT``


Syntaxe de base de l'instruction ``SELECT``
===========================================

..  code-block:: sql
    :linenos:

    SELECT
        <liste de colonnes>
    FROM
        <liste de tables>
    WHERE
        <condition de sélection>

Spécification des colonnnes sur lesquelles on projète
-----------------------------------------------------

Syntaxe de la partie ``<liste de colonnes>``
++++++++++++++++++++++++++++++++++++++++++++

La partie ``<liste de colonnes>`` qui spécifie les colonnes sur lesquelles projeter le résultat
de la requête peut prendre les formes suivantes :

..  list-table:: Syntaxe pour la spécification des colonnes à afficher (sur lesquelles on projète le résultat)
    :header-rows: 1
    :class: table-bordered table-responsive table-comparison

    *   - Syntaxe
        - Signification

    *   - ``colonne1, colonne2, ...``
        - liste des noms de colonnes séparés par des virgules

    *   - ``table1.*, table2.*, table3.col1``
        - Projeter sur toutes les colonnes des tables ``table1`` et ``table2`` ainsi que la la colonne ``col1`` de la table ``table3``

    *   - ``colonne1 AS [<en-tete-personnalisé>]``
        - La colonne ``colonne1`` portera l'en-tête ``<en-tete-personnalisé>`` dans le   résultat final

Spécification des tables à inclure dans la requête (produit cartésien)      
----------------------------------------------------------------------

Syntaxe de la partie ``<liste de tables>``
++++++++++++++++++++++++++++++++++++++++++++

La partie ``<liste de tables>`` de la clause ``FROM`` spécifie les tables dont
on forme le produit cartésien.

..  list-table:: Syntaxe pour la partie ``<liste de tables>`` de la clause ``FROM``
    :header-rows: 1
    :class: table-bordered table-responsive table-comparison

    *   - Syntaxe
        - Signification

    *   - ``table1, table2, ...``
        - la requête sera effectuée sur le produit cartésien :math:`\mathrm{table1} \times \mathrm{table2} \times \ldots`

    *   - ``table1 AS [<nouveau_nom>]``
        - la table ``table1`` sera connue sous le nom ``<nouveau_nom>`` dans le reste de la requête en particulier dans la partie ``<liste de colonnes>`` sur lesquelles on projète et dans la condition de la clause ``WHERE``.

Spécification des tables à inclure dans la requête (produit cartésien)      
----------------------------------------------------------------------

Syntaxe de la partie ``<condition de sélection>``
++++++++++++++++++++++++++++++++++++++++++++

La partie ``<condition de sélection>`` de la clause ``WHERE`` spécifie la
condition de sélection des lignes. Il s'agit d'une expression booléenne
formée d'une ou plusieurs conditions booléennes pouvant être combinées à
l'aides opérateurs logiques habituels faisant intervenir 

*   des noms de colonnes (souvent spécifiées sous la forme ``table.colonne``)

*   des expressions arithmétiques (addition / soustraction / multiplication / division / ...)

*   des opérateurs de comparaison

    *   ``<`` et ``>`` : inégalités strictes

    *   ``<=`` et ``>=`` : inégalités non strictes

    *   ``=`` : est égal à 

    *   ``<>`` : est différent de 




Apprendre par l'exemple
=======================

Vous allez surtout apprendre le SQL en observant attentivement des exemples et
en tentant de les reproduire dans d'autres contextes lors des exercices. 

Cette façon d'apprendre un nouveau langage est très courante en informatique.
Lorsque les exemples ne suffisent plus, on se réfère ensuite à la
documentation formelle du langage.

Affichage d'une table
---------------------

..  sql-connection-config:: sqlite:///bank.db

..  butreq::

    Afficher toutes les colonnes et toutes les lignes de la table ``client``.

..  sql::

    SELECT * FROM client


Projection
----------
..  butreq::

    Afficher uniquement les colonnes ``nom`` et ``prenom`` de la table ``client``

..  sql::

    SELECT nom, prenom 
    FROM client

..  butreq::

    Idem, mais en spécifiant les nom des tables

..  sql::

    SELECT client.nom, client.prenom 
    FROM client



Sélection
---------

..  butreq::

    Ne garder dans le résultat que les lignes qui vérifient la condition
    ``client.no_client > 3``

..  sql::

    SELECT *
    FROM client
    WHERE 
        client.no_client > 3


Plusieurs conditions de sélection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  butreq::

    Ne garder dans le résultat que les lignes qui vérifient la condition
    ``client.nom = 'Honegger'`` ET la condition ``client.prenom = 'Arthur'``

..  sql::

    SELECT *
    FROM client
    WHERE 
        client.nom = 'Honegger' 
        AND client.prenom = 'Arthur'

Opérateurs logiques et de comparaison
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  admonition:: Opérateurs logiques

    * ``AND`` : ET logique
    * ``NOT`` : NON logique
    * ``OR`` : OU logique (inclusif)

..  admonition:: Priorité des opérateurs logiques

    Dans une clause ``WHERE`` contenant plusieurs opérateurs booléens, ``NOT`` est
    évalué en premier, puis ``AND`` et finalement ``OR``.

..  admonition:: Opérateurs de comparaison

    * ``=`` : "est égal à"
    * ``>`` : "Strictement plus grand que"
    * ``<`` : "Strictement inférieur à"
    * ``<=`` : "Plus petit ou égal à"
    * ``>=`` : "Plus grand ou égal à"
    * ``<>`` : "Différent de"