############################################################################
Instruction ``UPDATE`` : Modifier des enregistrements de la base de données
############################################################################

L'instruction ``UPDATE`` permet de modifier un ou plusieurs enregistrements
d'une table.

Syntaxe
=======

..  sql::
    :no-output:

    UPDATE <table> SET col1 = expr1, col2 = expr2, etc ... WHERE <condition>

Tous les enregistrements de la table ``<table>`` qui satisfont aux
conditions ``<condition>`` 

..  admonition:: Documentation de référence pour SQLite

    Évidemment, la commande ``UPDATE`` présente encore bien des subtilités
    qui varient d'un SGBDR à l'autre. La syntaxe admise par SQLite est décrite 
    dans http://www.sqlite.org/lang_update.html .

Exemples
========

#)  Changer le prix du produit dont le numéro est 100

    ..  sql::
        :no-output:

        UPDATE produit
        SET prix_unitaire = 55.0
        WHERE produit_id = 100

#)  Augmenter de 10% le prix du produit dont le numéro est 100

    ..  sql::
        :no-output:

        UPDATE produit
        SET prix_unitaire = prix_unitaire * 1.1
        WHERE produit_id = 100        

#)  Diminuer de 5% le prix des produits dont le prix est supérieur à 50 CHF

    ..  sql::
        :no-output:

        UPDATE produit
        SET prix_unitaire = 0.95 * prix_unitaire
        WHERE prix_unitaire > 50

