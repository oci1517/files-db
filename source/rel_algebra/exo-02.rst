

Exercice 2 (Implémentation du produit cartésien)
================================================

..  only:: prof

    Question posables
    -----------------

    *   Que se passe-t-il si l'une des tables est vide

    *   Si la table1 a ``1000`` lignes et ``table2`` en comporte `2000`, quel est le
        le nombre de lignes dans le produit cartésien des deux tables ?

Consigne
--------        

Définir d'abord une fonction ``cartprod(table1, table2)`` qui retourne le
produit cartésien des tables ``table1`` et ``table2`` sous la forme d'une
nouvelle table.

Paramètres
----------

* ``table1`` : Liste de dictionnaires représentant une table

* ``table2`` : Liste de dictionnaires représentant une table

Valeur de retour
----------------

* La fonction doit retourner une table, représentée sous forme d'une liste de dictionnaire

* Le nombre de lignes dans la table produit cartésien est ``len(table1) * len(table2)``

*   La longueur d'une ligne de la table produit cartésien est ``len(record1) + len(record2)`` 
    où ``record1`` est un enregistrement de la table ``table1`` et ``record2`` un enregistrement de la 
    table ``table2``.


..  only:: not corrige

    Code de base
    ------------

    ..  code-block:: python

        def cartprod(table1, table2):
            result_table = []

            # votre code ici pour former le produit cartésien table1 x
            # table2

            return result_table


..  admonition:: Conseil

    Pour "concaténer" deux dictionnaires, on peut utiliser l'astuce
    suivante :

    ..  code:: python

        >>> dico1 = {1 : 'a', 2 : 'b'}
        >>> dico2 = {3 : 'c'}
        >>> grosdico = dict(list(dico1.items()) + list(dico2.items()))
        {1: 'a', 2: 'b', 3: 'c'}

    **Remarque** : L'ordre des éléments n'est pas nécessairement
    conservé dans ``grosdico``

Exemple
-------

Étant données les tables ``client`` et ``possession`` représentées par les
listes de dictionnaires ci-dessous,

..  code-block:: python

    client = [
        {'client.no_client': 1, 'client.prenom': 'Alan', 'client.nom': 'Turing'},
        {'client.no_client': 2, 'client.prenom': 'Arthur', 'client.nom': 'Honegger'},
        {'client.no_client': 3, 'client.prenom': 'Leonhard', 'client.nom': 'Euler'},
        {'client.no_client': 4, 'client.prenom': 'Berhard', 'client.nom': 'Riemann'},
        {'client.no_client': 5, 'client.prenom': 'John', 'client.nom': 'von Neuman'}
    ]

    possession = [
        {'possession.no_compte': 1, 'possession.no_client': 1},
        {'possession.no_compte': 1, 'possession.no_client': 2},
        {'possession.no_compte': 2, 'possession.no_client': 1},
        {'possession.no_compte': 3, 'possession.no_client': 2},
        {'possession.no_compte': 4, 'possession.no_client': 1},
        {'possession.no_compte': 5, 'possession.no_client': 4},
        {'possession.no_compte': 6, 'possession.no_client': 2},
        {'possession.no_compte': 7, 'possession.no_client': 2},
        {'possession.no_compte': 8, 'possession.no_client': 1},
        {'possession.no_compte': 9, 'possession.no_client': 4},
        {'possession.no_compte': 10, 'possession.no_client': 1},
        {'possession.no_compte': 11, 'possession.no_client': 2}
    ]

    def show_table(table):
        try:
            print(tuple(table[0].keys()))
            for r in table:
                print(tuple(r.values()))
        except:
            pass


on veut pouvoir calculer le produit cartésien

..  math::

    \mathrm{client} \times \mathrm{possession}

avec 

..  code-block:: python

    >>> grossetable = cartprod(client, compte)
    >>> show_table(grossetable)

et obtenir la sortie ::    

    ('possession.no_compte', 'possession.no_client', 'client.no_client', 'client.prenom', 'client.nom')
    (1, 1, 1, 'Alan', 'Turing')
    (1, 2, 1, 'Alan', 'Turing')
    (2, 1, 1, 'Alan', 'Turing')
    (3, 2, 1, 'Alan', 'Turing')
    (4, 1, 1, 'Alan', 'Turing')
    (5, 4, 1, 'Alan', 'Turing')
    (6, 2, 1, 'Alan', 'Turing')
    (7, 2, 1, 'Alan', 'Turing')
    (8, 1, 1, 'Alan', 'Turing')
    (9, 4, 1, 'Alan', 'Turing')
    (10, 1, 1, 'Alan', 'Turing')
    (11, 2, 1, 'Alan', 'Turing')
    (1, 1, 2, 'Arthur', 'Honegger')
    (1, 2, 2, 'Arthur', 'Honegger')
    (2, 1, 2, 'Arthur', 'Honegger')
    (3, 2, 2, 'Arthur', 'Honegger')
    (4, 1, 2, 'Arthur', 'Honegger')
    (5, 4, 2, 'Arthur', 'Honegger')
    (6, 2, 2, 'Arthur', 'Honegger')
    (7, 2, 2, 'Arthur', 'Honegger')
    (8, 1, 2, 'Arthur', 'Honegger')
    (9, 4, 2, 'Arthur', 'Honegger')
    (10, 1, 2, 'Arthur', 'Honegger')
    (11, 2, 2, 'Arthur', 'Honegger')
    (1, 1, 3, 'Leonhard', 'Euler')
    (1, 2, 3, 'Leonhard', 'Euler')
    (2, 1, 3, 'Leonhard', 'Euler')
    (3, 2, 3, 'Leonhard', 'Euler')
    (4, 1, 3, 'Leonhard', 'Euler')
    (5, 4, 3, 'Leonhard', 'Euler')
    (6, 2, 3, 'Leonhard', 'Euler')
    (7, 2, 3, 'Leonhard', 'Euler')
    (8, 1, 3, 'Leonhard', 'Euler')
    (9, 4, 3, 'Leonhard', 'Euler')
    (10, 1, 3, 'Leonhard', 'Euler')
    (11, 2, 3, 'Leonhard', 'Euler')
    (1, 1, 4, 'Berhard', 'Riemann')
    (1, 2, 4, 'Berhard', 'Riemann')
    (2, 1, 4, 'Berhard', 'Riemann')
    (3, 2, 4, 'Berhard', 'Riemann')
    (4, 1, 4, 'Berhard', 'Riemann')
    (5, 4, 4, 'Berhard', 'Riemann')
    (6, 2, 4, 'Berhard', 'Riemann')
    (7, 2, 4, 'Berhard', 'Riemann')
    (8, 1, 4, 'Berhard', 'Riemann')
    (9, 4, 4, 'Berhard', 'Riemann')
    (10, 1, 4, 'Berhard', 'Riemann')
    (11, 2, 4, 'Berhard', 'Riemann')
    (1, 1, 5, 'John', 'von Neuman')
    (1, 2, 5, 'John', 'von Neuman')
    (2, 1, 5, 'John', 'von Neuman')
    (3, 2, 5, 'John', 'von Neuman')
    (4, 1, 5, 'John', 'von Neuman')
    (5, 4, 5, 'John', 'von Neuman')
    (6, 2, 5, 'John', 'von Neuman')
    (7, 2, 5, 'John', 'von Neuman')
    (8, 1, 5, 'John', 'von Neuman')
    (9, 4, 5, 'John', 'von Neuman')
    (10, 1, 5, 'John', 'von Neuman')
    (11, 2, 5, 'John', 'von Neuman')


..  only:: corrige

    Corrigé
    -------

    ..  code-block:: python
        :linenos:

        def cartprod(table1, table2):
            result_table = []

            for r1 in table1:
                for r2 in table2:
                    r= dict(list(r1.items())+ list(r2.items()))

                    result_table.append(r)

                    # votre code ici pour former le produit cartésien table1 x table2

            return result_table