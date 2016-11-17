############################################################################
Instruction ``DELETE`` : Supprimer des enregistrements de la base de données
############################################################################

L'instruction ``DELETE`` permet de supprimer un ou plusieurs enregistrements
d'une table.

Syntaxe
=======

..  sql::
    :no-output:

    DELETE FROM <table> WHERE <condition>

Exemples
========

#)  Supprimer le client dont le ``client_id`` vaut 1

    ..  sql::
        :no-output:

        DELETE FROM client WHERE client_id = 1

#)  Supprimer les clients Fribourgeois

    ..  sql::
        :no-output:

        DELETE FROM client WHERE client.canton = 'FR'

#)  Supprimer les clients qui n'ont jamais passé de commande.

    ..  sql::
        :no-output:

        DELETE FROM client WHERE client_id NOT IN 
            (
                SELECT DISTINCT client.client_id
                FROM client, commande
                WHERE commande.client_id = client.client_id
            )

    ..  admonition:: Explication

        Dans cette requête imbriquée, on commence par déterminer les numéros
        de clients qui ont passé au moins une commande avec 

        ..  sql::

            SELECT DISTINCT client.client_id
            FROM client, commande
            WHERE commande.client_id = client.client_id

        Ensuite, on supprime tous les clients qui n'apparaissent pas dans
        cette liste à l'aide des opérateurs ``NOT IN``

