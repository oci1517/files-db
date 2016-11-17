Exercice 3 (Implémentation de la sélection)
===========================================

Consigne
--------        

Définir une fonction ``selection`` qui renvoie une copie de la table ``table``
qui ne contient que les enregistrements ``record`` de ``table`` pour
lesquels ``condition(record)`` est ``True``.

Paramètres
----------

* ``table`` : liste de dictionnaires

* ``condition`` : fonction qui prend en paramètre une ligne (dictionnaire)

..  only:: not corrige

    Code de base
    ------------

    ..  code-block:: python
    
        def selection(table):
            result_table = []

            # votre code ici pour ne garder de la table passée en argument
            # que les lignes à mettre dans le résultat finale

            return result_table


Exemple
-------

..  code-block:: python

    client = [
        {'client.no_client': 1, 'client.prenom': 'Alan', 'client.nom': 'Turing'},
        {'client.no_client': 2, 'client.prenom': 'Arthur', 'client.nom': 'Honegger'},
        {'client.no_client': 3, 'client.prenom': 'Leonhard', 'client.nom': 'Euler'},
        {'client.no_client': 4, 'client.prenom': 'Berhard', 'client.nom': 'Riemann'},
        {'client.no_client': 5, 'client.prenom': 'John', 'client.nom': 'von Neuman'}
    ]

    def show_table(table):
        try:
            print(tuple(table[0].keys()))
            for r in table:
                print(tuple(r.values()))
        except:
            pass

    def condition(record):
        return record['client.no_client'] > 2

    resultat = selection(client, condition)
    show_table(resultat)

produit la sortie ::    

    ('client.no_client', 'client.prenom', 'client.nom')
    (4, 'Berhard', 'Riemann')
    (5, 'John', 'von Neuman')

..  only:: corrige

    Corrigé
    -------

    ..  code-block:: python
        :linenos:

        def selection(table, condition):    
            result_table = []

            for record in table:
                if condition(record):
                    result_table.append(record)

            return result_table