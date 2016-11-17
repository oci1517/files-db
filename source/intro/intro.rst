*********************************
Introduction aux bases de données
*********************************

..  prof::

    ..  admonition:: 

        Gestion de cours 2011-2013 : https://docs.google.com/document/d/1I8YxMfl4A7jWpmcjbA-kn1FshqQmWgnLBZcaeq_O3tY/edit#heading=h.5h0f03fh7bcs

..  figure:: figures/logo-db.jpg
    :align: center
    :width: 80%

..  admonition:: Présentation PowerPoint du cours bases de données

    https://www.dropbox.com/home/CS/oc_inf/2013-2015/chapitres/9-bases-donnees?preview=Bases+de+donn%C3%A9es+relationnelles.pptx
    
Les bases de données sont aujourd'hui un sujet central de l'informatique
puisque les systèmes de gestion de bases de données constituent le centre
névralgique de notre société de l'information. Il ne passe pas un jour, pour
ne pas dire aucune seconde, sans que vous ayez, consciemment ou non, recours à
des bases de données pour effectuer des tâches quotidiennes.

Voici quelques activités quotidiennes qui nécessitent l'usage d'un système
d'information fondé sur des bases de données :

*   Se connecter à Facebook et consulter son mur
*   Envoyer un message sur Whatspapp
*   Chercher un numéro de téléphone dans le carnet d'adresse de son smartphone
*   Rechercher une correspondance sur le site des CFF
*   S'inscrire au Collège du Sud
*   Faire une requête sur Google
*   Faire un achat en ligne sur un site de e-commerce
*   etc ...
    
Les systèmes de gestion de bases de données sont capables de gérer des énormes
quantités de données (plusieurs Péta-octets !!!), de gérer les accès
concourrants à ces données par différents utilisateurs et de répondre en un
battement de cil à des centaines de requêtes (Le moteur de recherche Google répond à plusieurs dizaines de milliers de requêtes à la seconde ...).

Il est donc essentiel de comprendre le fonctionnement de base de ces systèmes
d'information et la manière d'organiser ces données pour pouvoir utiliser
toute cette puissance et espérer pouvoir monter une fois votre propre site de
e-commerce.

Bien qu'il existe de nombreuses façons d'organiser de grandes quantités de
données, nous étudierons le modèle relationnel qui a l'avantage d'être très
bien établi et qui fournira les bases pour comprendre d'autres familles de
bases de données comme les systèmes NoSQL de plus en plus en vogue dans le
monde de l'Internet (MongoDB).


Objectifs d'apprentissage
=========================

*   Comprendre les bases du modèle relationnel
*   Être capable de modéliser une situation concrète simple avec le modèle entités-associations
*   Être capable d'interroger un SGBDR (SQLite) à l'aide des instructions ``SELECT``, ``DELETE``, ``UPDATE`` du langage SQL
*   Être capable d'implémenter un schéma relationnel dans un SGBDR simple à l'aide des instructions DDL du langage SQL
*   Notions à comprendre

    -   Table / Relation
    -   Clé primaire / Clé étrangère
    -   association, cardinalité des associations
    -   types d'associations 

        +   Un à un
        +   Un à plusieurs
        +   Plusieurs à plusieurs

*   Être capable d'implémenter chaque type d'association dans le modèle relationnel
*   Comprendre la notion d'index d'une table et savoir comment ajouter un index à une table pour optimiser les recherches dans la table
*   Comprendre les bases de l'algèbre relationnelle
*   Être capable d'implémenter en Python les opérateurs de base de l'algèbre relationnelle

*   Être capable d'interroger une base de données SQLite depuis un programme Python