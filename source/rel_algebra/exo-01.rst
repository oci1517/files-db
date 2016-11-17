
..  _exo-algebre-relationnelle-exo-01:

Exercice 1 (théorique)
======================

..  only:: prof

    ..  admonition:: @prof TODO changement

        * Il faudra changer la donnée de cet exercice l'année suivante, de sorte
          que l'exercice soit faisable directement dans le cours et non avec
          15'000 fichiers annexes.

        * Une très bonne solution serait d'implémenter des fonctions 

            * ``selection``
            * ``projection``
            * ``cartesian_product``

          qui posent automatiquement les requêtes en SQL et retournent la table

        * Cet exercice n'est pas très pertinent. Le fait de traiter l'algèbre
          relationnel n'est d'ailleurs pas forcément très utile, hormis peut-
          être le fait de pouvoir faire des questions à l'oral        

Consigne
--------

Exprimez à l'aide des opérateurs relationnels les relations suivantes :

#)  Les numéros de comptes possédés par Arthur Honegger.

    ..  only:: corrige and not latex

        ..  only:: html

            ..  youtube:: aG2F9Ugkcz8
                :width: 100%

        ..  admonition:: Corrigé

            * Soit :math:`\mathrm{P} = \mathrm{possession}` et :math:`\mathrm{C} = \mathrm{client}`

            * Algèbre relationnelle :

                ..  math::
                    \pi_{\mathrm{P.no\_compte}}
                    \left(
                        \sigma_{
                            \substack{
                                \mathrm{C.no\_client} = \mathrm{P.no\_client} \wedge \\
                                \mathrm{C.nom = 'Honegger'} \wedge \\
                                \mathrm{C.prenom = 'Arthur'}
                            }
                        }
                        \left(
                            \mathrm{C} \times \mathrm{P}
                        \right)
                    \right)

            ..  only:: prof

                * en Python (à l'aide du module :file:`relational_algebra` disonible sur la Dropbox) :

                ..  code-block:: python

                    query['Exercice 1.a 1e étape'] = cartprod(R['CLIENT'], R['POSSESSION'])
                    query['Exercice 1.a 2e étape'] = selection(query['Exercice 1.a 1e étape'],
                                                                     '''r.CLIENT_no_client == r.POSSESSION_no_client
                                                                           and r.CLIENT_nom == "Honegger"
                                                                           and r.CLIENT_prenom == "Arthur" ''')
                    query['Exercice 1.a 3e étape'] = projection(query['Exercice 1.a 2e étape'],
                                                                ['POSSESSION_no_compte'])

            * Résultat

            ..  sqltable:: Comptes de Arthur Honegger
                :connection_string: sqlite:///bank.db
                :class: ocidbtable

                select
                    possession.no_compte as 'possession.no_compte'
                from client, possession
                where
                    client.no_client = possession.no_client
                    and client.nom = 'Honegger'
                    and client.prenom = 'Arthur'

#)  Les numéros de comptes possédés par Arthur Honegger ainsi que le montant
    que contient chaque compte.

    ..  only:: corrige and not latex

        ..  admonition:: Corrigé

            Dans cette question, on doit chercher des informations dans la table ``client`` (nom et prénom du client), ``possession`` qui indique quel compte appartient à quel client et ``compte`` qui indique le montant de chaque compte.

            * Soient les raccourcis :math:`\mathrm{P} = \mathrm{possession}`, :math:`\mathrm{C} = \mathrm{client}` et :math:`\mathrm{Co} = \mathrm{compte}`

            * Il faut donc commencer par effectuer le produit cartésien des
              trois tables :math:`\mathrm{P} \times \mathrm{C} \times
              \mathrm{Co}` qui donne lieu à une table gigantesque
              (http://sqlfiddle.com/#!7/d5dec/18)

            * Il faut, de cette gigantesque table, ne retenir que les lignes telles que 

                * :math:`\mathrm{P.no\_client} = \mathrm{C.no\_client}`
                * :math:`\mathrm{P.no\_compte} = \mathrm{Co.no\_compte}`
                * :math:`\mathrm{C.nom} = \mathrm{'Honegger'}`
                * :math:`\mathrm{C.prenom} = \mathrm{'Arthur'}`

              en opérant la sélection

                ..  math::

                    \sigma_{
                        \substack{
                            \mathrm{P.no\_client} = \mathrm{C.no\_client}  \\
                            \wedge \mathrm{P.no\_compte} = \mathrm{Co.no\_compte} \\
                            \wedge \mathrm{C.nom} = \mathrm{'Honegger'} \\
                            \wedge \mathrm{C.prenom} = \mathrm{'Arthur'} 
                        }
                    }
                    \left(
                        \mathrm{P} \times \mathrm{C} \times \mathrm{Co}
                    \right)

                * Lien : http://sqlfiddle.com/#!7/d5dec/20

            *   On termine par la projection qui permettra de ne garder que les colonnes
                désirées à savoir ``compte.no_compte`` et ``compte.montant``

                ..  math::

                    \pi_{
                        \mathrm{Co.no\_compte},
                        \mathrm{Co.montant}
                        }
                    \left( 
                    \sigma_{
                        \substack{
                            \mathrm{P.no\_client} = \mathrm{C.no\_client}  \\
                            \wedge \mathrm{P.no\_compte} = \mathrm{Co.no\_compte} \\
                            \wedge \mathrm{C.nom} = \mathrm{'Honegger'} \\
                            \wedge \mathrm{C.prenom} = \mathrm{'Arthur'} 
                        }
                    }
                    \left(
                        \mathrm{P} \times \mathrm{C} \times \mathrm{Co}
                    \right)
                    \right)

                * Lien : http://sqlfiddle.com/#!7/d5dec/22

            * Résultat

            ..  sqltable:: Comptes de Arthur Honegger avec leur montant
                :connection_string: sqlite:///bank.db
                :class: ocidbtable

                select 
                    possession.no_compte as 'possession.no_compte', 
                    compte.montant as 'compte.montant'
                from client, possession, compte
                where
                    client.no_client = possession.no_client 
                    and possession.no_compte = compte.no_compte
                    and client.nom = 'Honegger'
                    and client.prenom = 'Arthur'