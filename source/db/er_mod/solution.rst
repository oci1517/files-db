
..  only:: corrige

    ..  admonition:: Solution

        Après analyse des données à modéliser, nous nous apercevons que
        celles-ci sont formées de 6 entités (``LIVRE``, ``EDITEUR``, ``FOURNISSEUR``,
        ``EMPLOYE``, ``CLIENT`` et ``COMMANDE``) que nous pouvons directement représenter
        dans le diagramme sous la forme de rectangles. Une fois les entités
        posées, il y a lieu de s'interroger quant aux associations les reliant.
        En se référant à l'analyse des données du problème, on constate qu'il y
        a un lien de degré (1,n) entre les entités ``LIVRE`` et ``EDITEUR``, un lien de
        degré (1,n) entre les entités ``LIVRE`` et ``FOURNISSEUR``, un lien de degré (1,
        nc) entre les entités ``COMMANDE`` et ``CLIENT``, un lien de degré (n, nc) entre
        les entités ``COMMANDE`` et ``LIVRE`` et finalement un lien de type (nc, 1)
        entre les entités ``COMMANDE`` et ``EMPLOYE``. En assemblant ces différentes
        représentations, nous obtenons le modèle entités-associations suivant:

        ..  figures:: figures/modele5.jpg
            :align: center
            :width: 90%

            Une possibilité parmi d'autres pour le schéma entité-association 

..  only:: corrige

    ..  admonition:: Solution

        ..  figures:: figures/modele9.jpg
            :align: center
            :width: 90%

            Une possibilité parmi d'autres pour le schéma entité-association 

..  only:: corrige

    ..  admonition:: Solution

        ..  figures:: figures/modele7.jpg
            :align: center
            :width: 90%

            Une possibilité parmi d'autres pour le schéma entité-association 

