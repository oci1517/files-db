Exercice 5 (Interrogation de la base de données ``banque``)
=========================================================

..  only:: prof

    ..  admonition:: @prof : TODO

        Il faudrait rajouter une vidéo qui donne un exemple pour une requête
        simple à l'aide des opérateurs ``selection``, ``projection`` et
        ``cartprod``

..  _exo-algebre-relationnelle-exo-01-contexte:        

Contexte
--------

Les exercices suivants se basent sur la base de données de banque que vous
connaissez bien depuis le début de cours. Les tables de la base de données
sont représentées par des listes de dictionnaires :

..
    ..  actex:: relational-algebra-db-bank-definition

..  only:: not corrige

    ..  code-block:: python

        ###########################################################################
        ## Définition des tables sous forme de listes de dictionnaires
        ###########################################################################

        client = [
            {'client.no_client': 1, 'client.prenom': 'Alan', 'client.nom': 'Turing'},
            {'client.no_client': 2, 'client.prenom': 'Arthur', 'client.nom': 'Honegger'},
            {'client.no_client': 3, 'client.prenom': 'Leonhard', 'client.nom': 'Euler'},
            {'client.no_client': 4, 'client.prenom': 'Berhard', 'client.nom': 'Riemann'},
            {'client.no_client': 5, 'client.prenom': 'John', 'client.nom': 'von Neuman'}
        ]

        filiale = [
            {'filiale.no_filiale': 1, 'filiale.ville': 'Bulle', 'filiale.no': 1},
            {'filiale.no_filiale': 2, 'filiale.ville': 'Fribourg', 'filiale.no': 1},
            {'filiale.no_filiale': 3, 'filiale.ville': 'Lausanne', 'filiale.no': 1},
            {'filiale.no_filiale': 4, 'filiale.ville': 'Lausanne', 'filiale.no': 2},
            {'filiale.no_filiale': 5, 'filiale.ville': 'Zurich', 'filiale.no': 1},
            {'filiale.no_filiale': 6, 'filiale.ville': 'Zurich', 'filiale.no': 2},
            {'filiale.no_filiale': 7, 'filiale.ville': 'Zurich', 'filiale.no': 3}
        ]

        compte = [
            {'compte.no_filiale': 1, 'compte.montant': 500, 'compte.no_compte': 1, 'compte.date_acces': '01.01.2010'},
            {'compte.no_filiale': 1, 'compte.montant': 500, 'compte.no_compte': 2, 'compte.date_acces': '01.01.2010'},
            {'compte.no_filiale': 4, 'compte.montant': 700, 'compte.no_compte': 3, 'compte.date_acces': '03.04.2010'},
            {'compte.no_filiale': 3, 'compte.montant': 8000, 'compte.no_compte': 4, 'compte.date_acces': '05.07.2010'},
            {'compte.no_filiale': 1, 'compte.montant': 6000, 'compte.no_compte': 5, 'compte.date_acces': '05.10.2010'},
            {'compte.no_filiale': 1, 'compte.montant': 4000, 'compte.no_compte': 6, 'compte.date_acces': '23.02.2010'},
            {'compte.no_filiale': 2, 'compte.montant': 10000, 'compte.no_compte': 7, 'compte.date_acces': '15.04.2010'},
            {'compte.no_filiale': 3, 'compte.montant': 2300, 'compte.no_compte': 8, 'compte.date_acces': '12.10.2010'},
            {'compte.no_filiale': 2, 'compte.montant': 5600, 'compte.no_compte': 9, 'compte.date_acces': '23.06.2010'},
            {'compte.no_filiale': 6, 'compte.montant': 2300, 'compte.no_compte': 10, 'compte.date_acces': '11.10.2010'},
            {'compte.no_filiale': 4, 'compte.montant': 5400, 'compte.no_compte': 11, 'compte.date_acces': '01.01.2010'}
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


        ###########################################################################
        ## Opérateurs de l'algèbre relationnelle
        ###########################################################################

        def cartprod(table1, table2):
            ''' 

            Produit cartésien de ``table1`` avec ``table2`` qui sont les tables
            représentées par des listes de dictionnaires

            '''
            result_table = []

            for r1 in table1:
                for r2 in table2:
                    r= dict(list(r1.items())+ list(r2.items()))

                    result_table.append(r)

            return result_table

        def selection(table, condition):   
            ''' 

            Opérateur de sélection sur la table ``table``. Le paramètre
            ``condition`` est le nom d'une fonction qui prend en argument une
            ligne d'une table (donc un dictionnaire)

            '''
            result_table = []

            for record in table:
                if condition(record):
                    result_table.append(record)

            return result_table


        def projection(table, fields):
            ''' 

            Opérateur de projection de la table ``table`` sur les colonnes
            désignées par fields. Il faut que toutes les chaines de caractères
            présentes dans la liste ``fields`` correspondent à des clés des
            dictionnaires représentant les lignes de cette table.

            '''
            result_table = []

            for record in table:
                
                final_row = {}
                for (key, value) in record.items():
                    if key in fields:
                        final_row[key] = value

                # on ajoute la ligne à la table résultat une fois que la ligne a
                # été projetée sur les champs désirés
                result_table.append(final_row)
                
            return result_table   



Consigne
--------

Implémenter les expressions de l'algèbre relationnelle de l'exercice 
:ref:`exo-algebre-relationnelle-exo-01` en utilisant les fonctions ``cartprod``,
``selection`` et ``projection`` développées dans les exercices 2 à 4 qui sont définies
dans la partie :ref:`exo-algebre-relationnelle-exo-01-contexte`.

En d'autres termes, répondez à la question posée dans l'exercice 1.a en
complétant les fonctions ``query1a()`` et ``query1b()`` qui prend en argument
les tables ``client``, ``filiale``, ``compte``, ``possession`` présentées plus
haut.

..  admonition:: fonctions locales

    Vous remarquerez que le code de base des  ``query()`` disposent d'un
    squelette de fonction locale ``condition``. De la même manière qu'on peut
    définir des variables locales à l'intérieur d'une fonction, on peut y
    définir des fonctions locales.

    Cette fonction ``condition`` pourra ensuite être passée à l'opérateur
    ``selection(table, condition)``.

..  only:: not corrige

    ..  admonition:: Squelette de code

        Veuillez compléter les fonctions ``query1a()`` et ``query1b`` ci-dessous :


        ..  code-block:: python

            def query1a(client, filiale, compte, possession):
                '''

                Fonction retournant une table indiquant les éléments suivants : 

                * Les numéros de comptes possédés par Arthur Honegger (exercice 1a)

                '''

                # condition de sélection pour l'exercice 1a (à modifier pour
                # implémenter l'opération de sélection de l'exercice 1a)        
                def condition(r):
                    return True
                
                result_table = []

                # Votre code vient ici

                return result_table


            def query1b(client, filiale, compte, possession):
                '''

                Fonction retournant une table indiquant les éléments suivants : 

                * Les numéros de comptes possédés par Arthur Honegger ainsi que leur
                  montant (exercice 1b)

                '''    
                
                # condition de sélection pour l'exercice 1b (à modifier pour
                # implémenter l'opération de sélection de l'exercice 1b)   
                def condition(r):
                    return True
                
                result_table = []

                # Votre code vient ici


                return result_table

            # Exercice 1a
            print("Requête de l'exercice 1a")
            show_table(query1a(client, filiale, compte, possession))

            # Exercice 2a
            print("Requête de l'exercice 1b")
            show_table(query1b(client, filiale, compte, possession))        


..  only:: corrige

    ..  admonition:: Corrigé

        ..  code-block:: python

            def query1a(client, filiale, compte, possession):
                
                # condition de sélection pour l'exercice 1a
                def condition(r):
                    return (r['client.no_client'] == r['possession.no_client'] \
                           and r['client.nom'] == 'Honegger' \
                           and r['client.prenom'] == 'Arthur')
                
                result_table = []

                result_table = projection(selection(cartprod(client, possession),
                                                    condition),
                                         ['possession.no_compte'])

                return result_table


            def query1b(client, filiale, compte, possession):
                
                # condition de sélection pour l'exercice 1b
                def condition(r):
                    return (r['client.no_client'] == r['possession.no_client'] \
                        and r['compte.no_compte'] == r['possession.no_compte'] \
                       and r['client.nom'] == 'Honegger' \
                       and r['client.prenom'] == 'Arthur')
                
                result_table = []

                grossetable = cartprod(cartprod(client, possession), compte)

                result_table = projection(selection(grossetable, condition),
                                         ['compte.no_compte', 'compte.montant'])

                return result_table

            # Exercice 1a
            print("Requête de l'exercice 1a")
            show_table(query1a(client, filiale, compte, possession))

            # Exercice 2a
            print("Requête de l'exercice 1b")
            show_table(query1b(client, filiale, compte, possession))        