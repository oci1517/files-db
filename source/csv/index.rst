############
Formats de fichiers
############

En pratique, il existe certains formats de données assez répandus pour stocker
des données dans des fichiers (flat files). Les plus répandus sont le formats
CSV qui permet de stocker des données tabulaires et le format XML (eXtended
Markup Language) qui permet de stocker des données fortement structurées.

Format CSV
==========

Aperçu du format
----------------

Le format CSV (Comma Seperated Values) est un format standard pour stocker des
données de nature tabulaires. Les tableurs tels que Excel disposent d'ailleurs
d'une fonctionnalité permettant d'exporter / importer des données vers et à
partir de fichiers CSV).

Voici un exemple de fichier CSV qui représente des données tabulaires
représentant le catalogue d'une librairie.

.. literalinclude:: files/sample.csv
   :language: csv

Voici une représentation tabulaire de ce fichier CSV :

.. csv-table:: Représentation tabulaire du fichier ``sample.csv``
   :file: files/sample.csv
   :delim: ;
   :header-rows: 1

.. admonition:: Données CSV réelles

   Le site https://support.spatialkey.com/spatialkey-sample-csv-data/ met à
   disposition des exemples de fichiers CSV contenant des données réelles

Avantages et désavantages du format CSV
---------------------------------------

Les avantages principaux du format CSV sont les suivants

*  Extrême simplicité
*  Supporté par de très nombreux logiciels (dont Excel)
*  Il est très facile de charger ces données dans un programme (cf. exercice 1)

Les désavantages principaux du format CSV sont les suivants

*  Comme les champs sont séparés par un caractère de séparation défini, par exemple ``;`` ou ``,``, ce caractère ne peut pas figurer dans les champs stockés à proprement parler, pour la même raison qu'une chaine de caractères Python délimitée par ``"`` ne peut pas contenir un caractère ``"``.

   Par exemple, les données suivantes ne constituent pas du CSV valide (caractère de séparation utilisé : ``:``)

   ::

      Nom:Prenom:Commentaire
      Van Rossum:Guido:Créateur de Python : un vrai génie

   En effet, le troisième champ de la ligne concernant Guido Van Rossum contient un double point alors qu'il s'agit du caractère de délimitation entre les champs.

Modules Python pour gérer du CSV
--------------------------------

Il existe différents modules Python permettant de charger des données sous forme
de fichier CSV. Voici les plus populaires :

*  Le module ``csv`` intégré à Python (documentation officielle : https://docs.python.org/3/library/csv.html)
*  Le module ``fastcsv``, bien plus rapide que la version intégrée à Python pour de gros fichiers (https://github.com/draftcode/fastcsv), voir la discussion http://softwarerecs.stackexchange.com/questions/7463/fastest-python-library-to-read-a-csv-file

.. admonition:: Tutoriels avancés de gestion de CSV en python
   :class: tip

   *  https://newcircle.com/s/post/1572/python_for_beginners_reading_and_manipulating_csv_files

Le format XML
=============

Le format XML est bien plus compliqué à définir car il est beaucoup plus
flexible et puissant. Ce qu'il faut savoir c'est qu'il permet de stocker des
données structurées de manière bien plus appropriée que le CSV qui contraint
toutes les données à suivre un même schéma.

Le XML est tellement flexible qu'il oblige à définir la manière dont les données
sont stockées (c'est le rôle du fameux DTD).

Les fichiers documents OpenDocumentFormat (odf) de LibreOffice sont constitués
entièrement de données XML. Voici par exemple à quoi un fichier "Writer" créé
dans LibreOffice contenant simplement le texte "Exemple de fichier ODT" (ligne 46):

.. literalinclude:: files/odt/content.xml
   :language: xml
   :linenos:


.. admonition:: Remarques

   Vous comprenez pourquoi le XML est assez délicat à utiliser et pourquoi il faut
   impérativement recourir à une bibliothèque permettant d'utiliser ce format très
   verbeux et compliqué.

   Remarquez la ressemblance entre le XML et le HTML. Tous deux sont en fait de
   parenté puisque le HTML est une sorte de XML dégénéré, moins pointilleux. XML
   et HTML sont des languages à balises qui délimitent les données par des
   balises ``<balise-ouvrante>CONTENU</balise-fermante>``.

Exercices
=========

Exercice 1
----------

Télécharger le fichier :download:`files/sample.csv` et écrire un programme
Python qui charge ce fichier CSV en mémoire, en fait l'analyse syntaxique
(parsing). Le programme demande ensuite à l'utilisateur d'insérer un numéro de
produit et affiche les données concernant l'article en question. Si l'article
n'est pas contenu dans le fichier CSV, afficher un message d'erreur et demander à
l'utilisateur d'insérer un autre numéro

.. admonition:: Exemple d'interaction

   ::

      Numéro de produit :
      > 200

      Détails du produit
      ------------------

      Description : Dieux du stade
      Reliure : Cartonné
      Prix unitaire : 100.0

      Numéro de produit :
      > 155

      Produit inconnu !!!

      Numéro de produit :
      >


Exercice 2
----------

On donne les listes suivantes :

::

   headers = ['Nom', 'Prénom', 'courriel']
   data = [
      ('Donner', 'Cédric', 'donner@example.com'),
      ('Van Rossum', 'Guido', 'guido@python.com'),
      ('Einstein', 'Albert', 'albert@relativity.com'),
      ('Von Neumann', 'John', 'gametheory.com'),
   ]

Développer un petit programme qui enregistre ces données de manière intelligente
au format CSV dans le fichier ``emails.csv``. Choisir un caractère de séparation
approprié.


Exercice 3 (*)
----------

Télécharger le fichier
:file:`S:\\CSUD\\Partage-Eleves\\Disciplines\\Informatique_OC\\edt.csv` se trouvant
dans le dossier ``Partage-Eleves`` du serveur du Collège du Sud. Il est placé à
cet endroit car il contient des données qui ne peuvent pas être publiées sur
Internet pour des raisons de confidentialité. Il s'agit des attributions des
cours dans les salles de classe pour l'année 2016-2017 au Collège du Sud, au
format CSV.

*  Autre lien de téléchargement : :download:`files/edt.zip` (demander le mot de passe par courriel)
