
Exercices
=========

Exercice 1
----------

Rechercher les anagrammes dans le fichier ``words-1$.txt`` (deux mots possédant
exactement les mêmes lettres mais dans un ordre différent, par exemple maison et
aimons) en ignorant la casse. Écrire les anagrammes que vous avez trouvés dans
un fichier ``anagram.txt``.

.. admonition:: Remarque
   :class: note

   Testez également votre algorithme sur les fichiers suivants :

   *  ``tjwordlist/english/words-2.txt``
   *  ``tjwordlist/english/words-3.txt``
   *  ``tjwordlist/multilingual/moby/french.txt``

   Normalement, si votre algorithme est efficace, cela ne devrait pas prendre
   plus de 1 seconde sur un ordinateur récent.

   Attention à la gestion des accents avec le fichier ``french.txt``. Établir
   une stratégie pertinente pour gérer les caractères accentués-.

.. only:: corrige

   .. admonition:: Corrigé

      Code source :

      .. literalinclude:: solutions/ex01.py
         :language: python3
         :linenos:

      Sortie :

      .. literalinclude:: solutions/out-ex01-words-3.txt
         :linenos:
         :lines: 1-10


Exercice 2
----------

.. sidebar:: Utilisation des anagrammes par Galilée

   Les anagrammes étaient déjà utilisés par Galilée pour garder le secret de ses
   découvertes scientifiques

Le texte suivant a été crypté par anagramme : les mots originaux ont été
substitués par des mots dont les lettres sont permutées.

::

   IINFHS SOLOHC AEMK SIWREKOFR

Décrypter ce texte à l’aide de la liste de mots (``words-1$.txt``)


Exercice 3
----------

Créer votre propre texte crypté pouvant être décrypté de manière non ambigüe à
l’aide de la liste de mots.

Exercice 4
----------

Modifier l'exercice 1 ou deux en utilisant des gestionnaires des contexte pour
ouvrir le fichier.
