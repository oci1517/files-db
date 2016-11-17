#######################################
Persistence des données dans les fichiers
#######################################

Introduction
============


Les informations stockées informatiquement, appelées données, jouent un rôle
crucial dans notre société high-tech actuelle. Bien que ces informations soient
comparables à du texte écrit, elles comportent également quelques différences
notables :

*  Les données ne peuvent être lues, stockées et traitées qu’à l’aide d’un **système informatique**

*  Les données sont toujours codées **sous forme binaire** à l’aide de 0 et de 1.
   Elles ne représentent des informations intelligibles que dans la mesure où
   elles sont correctement interprétées (décodées).

*  Les données possèdent une certaine **durée de vie**. Au sein même d’un programme,
   les données n’ont qu’une durée de vie temporaire, limitée à l’exécution d’un
   bloc de code en ce qui concerne les variables locales ou à la durée de vie du
   programme en ce qui concerne les variables globales. Les données
   persistantes, quant à elles, ont une durée de vie qui transcende l’exécution
   du programme et peuvent être récupérées après son exécution.

*  Les données possèdent une certaine **visibilité (disponibilité)**. Alors que
   certaines données personnelles peuvent être lues par n’importe qui sur un
   réseau social, il existe également des données privées ou d’autres types de
   données figurant sur des supports de données non accessibles au le grand
   public.

*  Les données peuvent être **protégées**. La protection des données peut être
   réalisée à l’aide du **cryptage** ou de **restrictions d’accès** (protection par mot
   de passe).

*  Les données peuvent être facilement transportées et transférées par des
   **canaux de communication digitaux**.

*  Les données persistantes peuvent être écrites ou lues par les programmes
   informatiques sous la forme de fichiers sur des supports de stockage
   physiques (Disques durs (HDD = Hard drive disk), disques SSD (= Solid State
   Drive), cartes mémoires ou clés USB. Un fichier est constitué de zones de
   stockage au sein d’une certaine structure (système de fichiers) et suivant un
   **format de données** bien précis. Du fait que le transfert de fichiers est
   devenu rapide et bon marché même sur de très longues distances, les fichiers
   sont de nos jours de plus en plus stockés sur des supports distants (**stockage dans le nuage**).

Les fichiers sont gérés sur l’ordinateur au sein d’une structure de dossiers
hiérarchique dans laquelle chaque dossier particulier peut contenir non
seulement des fichiers mais également des sous-dossiers. Les fichiers sont
accessibles à l’aide de leur **chemin d'accès** (*file path* en anglais) contenant le
nom de tous les dossiers parents ainsi que le nom du fichier. Le système de
fichiers est cependant **dépendant du système d’exploitation**, ce qui explique
qu’il existe de grandes différences entre les systèmes Windows, Mac et Linux.


.. admonition:: Concepts de programmation
   :class: tip

   *  Encodage
   *  durée de vie
   *  visibilité de données
   *  fichier


Lire et écrire des fichiers texte
=================================


.. sidebar::  Gestion des sauts de ligne sous Windows

   Sous Windows, si on lit un fichier texte ou une ligne que l’on stocke dans
   une chaine de caractères, les caractères ``\r`` (retour charriot) spécifiques à
   Windows sont écartés. Lors de l’écriture d’une chaine de caractères dans un
   fichier, ceux-ci sont à nouveau rajoutés automatiquement. Cela permet dans
   une large mesure d’atteindre au sein du programme un code indépendant de la
   plateforme utilisée pour l’exécution.

Nous avons déjà vu comment lire des fichiers texte dans le chapitre Internet.
Dans les fichiers texte, les caractères sont stockés de manière séquentielle
mais il est possible d’obtenir une structure de fichiers ligne par ligne
similaire à celle apparaissant sur une feuille de papier grâce au caractère de
fin de ligne ``\n``. Et c’est là que le bât blesse, en raison de la différence
d’encodage du saut de ligne sur les différents systèmes d’exploitation : alors
que les systèmes Mac et Linux utilisent le caractère ASCII <line feed> (EOL),
Windows utilise une combinaison de <carriage return><line feed>. En Python, ces
caractères sont codés à l’aide des séquences d’échappement ``\r`` et ``\n``


.. raw:: html

   <div class="clearfix"></div>

.. sidebar:: Palindrome

   Un **palindrome** est un mot qui se lit exactement de la même manière en allant de
   gauche à droite ou de droite à gauche, sans considération de la casse (pas de
   différence entre majuscules ou minuscules).

   **Référence** : https://fr.wikipedia.org/wiki/Palindrome

Le programme suivant va utiliser un dictionnaire anglais disponible sous la
forme d’un fichier texte qui est téléchargeable (tfwordlist.zip) depuis le lien
http://www.tigerjython.ch/download/tjwordlist.zip. Il faut décompresser
l’archive zip et copier le fichier ``words-1$.txt`` dans le dossier dans lequel se
trouve le programme Python. Vous allez devoir déterminer, parmi tous les mots
contenus dans le dictionnaire en question, lesquels sont des **palindromes**.


.. raw:: html

   <div class="clearfix"></div>


La fonction ``open()`` retourne un objet fichier fqui permet de manipuler le fichier à
proprement parler. Cet objet fichier permet par exemple de parcourir le fichier
ligne à ligne à l’aide d’une boucle ``for``. Il est de ce fait capital de noter que
chaque ligne se termine par un caractère de fin de ligne ``\n`` qui doit être ôté
par une opération de slicing appropriée avant que le mot ne soit lu en sens
inverse. De plus, afin de ne pas distinguer les majuscules et minuscules, il
faut commencer par convertir tous les caractères en minuscules grâce à la
fonction ``lower()``.

En Python, il existe une astuce pour retourner une chaîne à l’envers puisque
l’opérateur de slicing accepte également des indices négatifs qui débutent alors
l’indexage de la chaine depuis la fin. Ainsi, si l’on parcourt la chaine avec un
pas de ``-1``, la chaine est parcourue à l’envers.

.. code-block:: python
   :linenos:

   def isPalindrom(a):
      return a == a[::-1]

   f = open("worte-1$.txt")

   print("Searching for palindroms...")
   for word in f:
      word = word[:-1] # remove trailing \n
      word = word.lower() # make lowercase
   if isPalindrom(word):
        print(word)
   f.close()
   print("All done")

La méthode ``readline()`` permet de lire le fichier ligne à ligne. Il faut
s’imaginer un pointeur qui progresse dans le fichier lors de chaque appel de la
fonction. Dès que l’on a atteint la fin du fichier, la méthode retourne une
chaîne vide. Le programme sauve ensuite la liste des palindromes dans un fichier
``palindrom.txt``. Mais avant de pouvoir écrire dans un fichier, il faut
l’ouvrir à l’aide de la fonction ``open()`` en passant la chaine de caractères
``"w"`` (pour *write* = écrire) en tant que second argument. Il est ensuite
possible d’écrire vers le fichier à l’aide de la méthode ``write()``. Il est
impératif de ne pas oublier d’appeler la méthode ``close()`` à la fin de l’écriture
pour être certain que l’ensemble des caractères aient été écrits vers le fichier
et que le système d’exploitation ait libéré les ressources nécessaires à
l’opération.


.. code-block:: python
   :linenos:

   def isPalindrom(a):
      return a == a[::-1]

   fInp = open("worte-1$.txt")
   fOut = open("palindrom.txt", "w")

   print("Searching for palindroms...")
   while True:
   word = fInp.readline()
   if word == "":
        break
   word = word[:-1] # remove trailing \n
   word = word.lower() # make lowercase
   if isPalindrom(word):
        print(word)
        fOut.write(word + "\n")
   fInp.close()
   fOut.close()
   print("All done")


.. admonition:: Memento
   :class: warning

   Lors de l’ouverture d’un fichier texte avec ``open(path, mode)``, le mode
   utilisateur (*user mode*), est spécifié sous forme de chaine de caractères grâce
   au paramètre mode.

   .. list-table:: Ouverture d'un fichier
      :header-rows: 1

      -  *  Mode
         *  Description
         *  Commentaire

      -  *  ``"r"`` (read)
         *  Lecture seule
         *  Le fichier doit exister. Il s’agit de la **valeur par défaut**.

      -  *  ``"w"`` (write)
         *  Ouverture en écriture: le fichier est créé s’il n’existe pas encore et on peut y écrire des données.
         *  Si le fichier existe déjà, son contenu est écrasé.

      -  *  ``"a"`` (append)
         *  Ajoute les données écrites à la fin du fichier.
         *  Le fichier est créé s’il n’existe pas encore.

      -  *  ``"r+"``
         *  Accès en lecture et en écriture avec concaténation. Le contenu est ajouté à la fin du contenu déjà existant.
         *  Le fichier doit déjà exister.


   Pour recommencer la lecture du fichier une fois que le pointeur de lecture
   est parvenu à la fin du fichier, il faut soit fermer le fichier et le rouvrir
   ou simplement appeler la méthode ``seek(0)`` de l’objet fichier retourné par
   ``open()``. Il est également possible de lire en une seule fois tout le contenu
   du fichier et récupérer son contenu sous forme de chaine de caractères avec

   ::

      text = f.read()

   sans oublier de fermer le fichier avec ``f.close()``. Il est également possible
   d’obtenir une liste de toutes les lignes contenues dans le fichier, sans les
   sauts de ligne, avec

   ::

      textList = text.splitlines()

   Voici encore quelques opérations importantes sur les fichiers :

   ::

      import os
      os.path.isfile(path)

   Retourne ``True`` si le fichier path existe.

   ::

      import os
      os.remove(path)

   Supprime le fichier path.


Sauver et restaurer des options et des données de jeu
=====================================================

Les fichiers sont fréquemment utilisés pour sauvegarder des informations dans le
but de pouvoir les réutiliser lors d’une exécution ultérieure du programme. Il
s’agit très souvent de paramètres de configuration apportés par l’utilisateur
dans un but de personnalisation. Il se pourrait également que l’on veuille
sauver l’état actuel d’un jeu pour pouvoir reprendre la partie ultérieurement en
repartant de l’état exact dans lequel le jeu avait été laissé.

En général, les options de configuration et l’état d’un programme sont sauvés de
manière très naturelle par des paires clé-valeur où la clé permet d’identifier
sans ambiguïté la valeur. L’IDE TigerJython comporte par exemple quelques
options de configuration qu’il est utile de connaître:

.. csv-table:: Paires clé-valeur présentes dans l'environnement TigerJython
   :header-rows: 1
   :delim: ;

   Clé;Valeur
   ``"autosave"``;``True``
   ``"language"``;``"fr"``

Comme nous l’avions vu au chapitre 6.3, il est possible de sauver de telles
paires clé-valeur dans un dictionnaire Python que l’on peut ensuite stocker et
récupérer sous forme binaire à l’aide du module ``pickle``. Avant de fermer la
fenêtre, le programme ci-dessous sauvegarde la position et la direction
actuelles du crabe ainsi que la position du curseur de vitesse de la simulation.
Ces données ainsi sauvées seront lues et restaurées lors du prochain démarrage
du jeu.

.. code-block:: python
   :linenos:

   import pickle
   import os
   from gamegrid import *

   class Lobster(Actor):
      def __init__(self):
         Actor.__init__(self, True, "sprites/lobster.gif");

      def act(self):
         self.move()
         if not self.isMoveValid():
             self.turn(90)
             self.move()
             self.turn(90)

   makeGameGrid(10, 2, 60, Color.red)
   addStatusBar(30)
   show()

   path = "lobstergame.dat"
   simulationPeriod = 500
   startLocation = Location(0, 0)
   if os.path.isfile(path):
      inp = open(path, "rb")
      dataDict = pickle.load(inp)
      inp.close()
      # Reading old game state
      simulationPeriod = dataDict["SimulationPeriod"]
      loc = dataDict["EndLocation"]
      location = Location(loc[0], loc[1])
      direction = dataDict["EndDirection"]
      setStatusText("Game state restored.")
   else:
      location = startLocation
      direction = 0

   clark = Lobster()
   addActor(clark, startLocation)
   clark.setLocation(location)
   clark.setDirection(direction)
   setSimulationPeriod(simulationPeriod)

   while not isDisposed():
      delay(100)
   gameData = {
      "SimulationPeriod": getSimulationPeriod(),
      "EndLocation": [clark.getX(), clark.getY()],
      "EndDirection": clark.getDirection()
   }
   out = open(path, "wb")
   pickle.dump(gameData, out)
   out.close()
   print "Game state saved"

.. admonition:: Memento
   :warning:

   Il est possible de sauvegarder un dictionnaire vers un fichier binaire à l’aide
   de la méthode ``pickle.dump()``. Comme le fichier est au format binaire, il est
   impossible de l’ouvrir dans un éditeur et de le modifier.


Gestion pythonique des fichiers
===============================

Il existe une manière plus pythonique de gérer les entrées-sorties sur les
fichiers en utilisant un **gestionnaire de contexte** (*context manager*). Cela
consiste à utiliser un bloc ``with`` qui a l'avantage de se charger
automatiquement de la fermeture du fichier (appel à la méthode ``.close()`` du
descripteur de fichier), même en cas de plantage du programme.

.. code-block:: python3

   with open("file.text", "r", encode="utf-8") as fd:
      for line in fd:
         print(line)

.. admonition:: Remarque

   Notez bien qu'il n'y a pas d'appel à la méthode ``fd.close()``. Celle-ci est
   appelée automatiquement par le gestionnaire de contexte lorsque le bloc
   ``with`` est terminé.

.. include:: exos.rst
