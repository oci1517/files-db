Exercice 4 (Implémentation de la projection)
============================================

Consigne
--------        

Définir une fonction ``projection`` qui renvoie une nouvelle table
correspondant à ``table`` dont on ne garde que les champs (colonnes) indiqués
dans la     liste ``fields``.

Paramètres
----------

* ``table`` : liste de dictionnaires

* ``fields`` : liste de chaines de caractères indiquant les champs sur lesquels projeter la table

..  only:: not corrige

    Code de base
    ------------

    ..  code-block:: python

        def projection(table, fields):
            result_table = []

            # votre code ici pour ne garder que les colonnes utiles dans
            # le résultat final

            return result_table


Exemple
-------

Pour les exemples suivants, considère la liste de dictionnaires ``client`` qui
représente la table ``client`` et la fonction ``show_table(table)`` définies
par le code suivant :

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

Exemple 1
~~~~~~~~~

L'exemple suivant montre comment effectuer l'opération de projection

..  math::

    \pi_{
        \mathrm{client.nom, client.prenom}
    }
    \left(
        \mathrm{client}
    \right)

..  code-block:: python

    >>> resultat = projection(client, fields=['client.nom', 'client.prenom'])
    >>> show_table(resultat)
    ('client.prenom', 'client.nom')
    ('Alan', 'Turing')
    ('Arthur', 'Honegger')
    ('Leonhard', 'Euler')
    ('Berhard', 'Riemann')
    ('John', 'von Neuman')

Exemple 2
~~~~~~~~~

L'exemple suivant montre comment effectuer l'opération de projection

..  math::

    \pi_{
        \mathrm{client.nom}
    }
    \left(
        \mathrm{client}
    \right)

..  code-block:: python

    >>> resultat = projection(client, fields=['client.nom'])
    >>> show_table(resultat)
    ('client.nom',)
    ('Turing',)
    ('Honegger',)
    ('Euler',)
    ('Riemann',)
    ('von Neuman',)


..  only:: corrige

    Corrigé
    -------

    ..  code-block:: python
        :linenos:

        def projection(table, fields):
            result_table = []

            # votre code ici pour ne garder que les colonnes utiles dans le
            # résultat final
            for record in table:
                
                final_row = {}
                for (key, value) in record.items():
                    if key in fields:
                        final_row[key] = value

                # on ajoute la ligne à la table résultat une fois que la ligne
                # a été projetée sur les champs désirés
                result_table.append(final_row)
                
            return result_table