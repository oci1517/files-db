###########################################################
Instruction ``INSERT`` : insérer des données dans une table
###########################################################

La commande SQL ``INSERT`` permet d’insérer de nouveaux enregistrements dans
une table.

Syntaxe
=======

..  sql::
    :no-output:

    INSERT INTO <nom_table> (<liste_champs>) VALUES (<liste_valeurs>)

..  admonition:: Remarque

    *   La liste des champs doit contenir les noms des champs auxquels une valeur sera
        affectée dans la liste des valeurs.

    *   Si la clé primaire est du type ``AUTOICREMENT``, il n'est pas nécessaires de 
        spécifier la clé primaire : c’est le SGBD qui s’en chargera automatiquement.

    *   Les champs spécifiés dans ``<liste_champs>`` doivent correspondre exactement, 
        dans l’odre, aux valeurs spécifiées dans ``<liste_valeurs>``.

Exemples
========

#)  Insérer le client Dupond dans la table ``client``

    ..  sql::
        :no-output:

        INSERT INTO client
            (nom, adress, canton, no_postal, ville)
        VALUES
            ('Dupond', 'Rue du Moulin 8', 'FR', 1630, 'Bulle');

    ..  admonition::    Remarque

        On a omis de spécifier le champ ``no_client`` car il s'agit d'une clé
        primaire autoincrémentée par le SGBDR. En d'autres termes, c'est le
        SGBDR qui se charge d'attribuer un numéro unique à chaque client.

#)  Insérer le client Dupont en ne spécifiant que le nom du client et le canton

    ..  sql::
        :no-output:

        INSERT INTO client
            (canton, nom)
        VALUES
            ('FR','Dupont');

    Dans ce cas, tous les champs qui ne sont pas spécifiés seront remplacés par la
    valeur ``NULL``, ou par la valeur par défaut si elle a été spécifiée lors de la
    définition de la table par la contrainte de champ ``DEFAULT``.

Exercice (Génération d'instructions ``SQL``)
============================================

Consignes
---------

On donne le fichier :file:`client.csv` contenant les données des clients de
notre base de données :file:`library.db` comme suit :

::

    no_client;nom;adresse;ville;canton;no_postal
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


Développez un programme python qui, à partir des données de ce fichier, va
générer les requêtes SQL ``INSERT`` nécessaires pour insérer les données dans
la table ``client`` et écrire ces instructions ``INSERT`` dans un fichier
:file:`client_insert.sql`.

..  admonition:: Remarque

    *   La première ligne du fichier spécifie l'ordre des valeurs dans les lignes
        suivantes. 

    *   Il vous est demandé de tenir compte de cette première ligne : votre
        programme doit fonctionner correctement même si les champs ne sont pas 
        spécifiés dans le même ordre.

    *   Votre programme doit donc également être capable de traiter le fichier
        suivant qui spécifie le nom du client en dernier champ sur chaque ligne :

        ::

            no_client;adresse;ville;canton;no_postal;nom
            1;2 Lindenstrasse;Zürich;ZH;8000;Archambault
            2;10 route du Jura;Fribourg;FR;1700;Au plaisir de Lire

..  tip::

    Les instructions DDL de définition de la table ``client`` se trouvent dans 
    :ref:`sec-databases-show-library`


..  only::   corrige

    Corrigé
    -------

    Voici un code que l'on peut utiliser 

    ..  literalinclude:: code/csv2sql/csv2sql.py
        :language: python
        :linenos:

    Remarques
    ---------

    Le code précédent appelle quelques remarques :

    #)  On utiliser les fonctions ``escape_quotes`` pour éviter des problèmes
        avec les chaines de caractères contenant des apostrophes ``'``. En effet,
        la requête suivant poserait problème :

        ::

            INSERT INTO client ( no_client, nom, adresse, ville, canton, no_postal )
            VALUES ( '14', 'Librairie de l'Université', '6 Haldenstrasse', 'Berne', 'BE', '3000' );

        car le nom du client contient une apostrophe. Il faut corriger la
        requête en mettant une double apostrophe, ce dont se charge la
        fonction ``escape_quotes`` :

        ::

            INSERT INTO client ( no_client, nom, adresse, ville, canton, no_postal )
            VALUES ( '14', 'Librairie de l''Université', '6 Haldenstrasse', 'Berne', 'BE', '3000' );

    #)  La fonction ``add_quotes`` ajoute des apostrophes autour de toutes les
        valeurs insérées dans la base de données

    #)  On utilise un "template" SQL, défini à la ligne 27, traité aux lignes 36 - 38


    Instructions SQL ``INSERT`` générées
    ------------------------------------

    Voici le contenu du fichier ``client_insert.sql`` généré par le programme :

    ..  literalinclude:: code/csv2sql/client_insert.sql
        :language: sql
