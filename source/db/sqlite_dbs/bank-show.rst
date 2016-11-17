###########################################
Contenu de la base de données ``bank.db``
###########################################

..  admonition:: Lien SQLFiddle.com

    http://sqlfiddle.com/#!7/d6675

Liste des tables
================

..  code-block:: sql

    SELECT name FROM sqlite_master WHERE type = 'table' and NOT name LIKE 'sqlite_%'

..  sqltable:: 
    :connection_string: sqlite:///bank.db
    :class: ocidbtable

    SELECT name FROM sqlite_master WHERE type = 'table' and NOT name LIKE 'sqlite_%'

Contenu des tables
==================

..
    Table ``{table}``
    -----------------

    ..  code-block:: sql

        SELECT * FROM {table}

    ..  sqltable:: 
        :connection_string: sqlite:///bank.db
        :class: ocidbtable

        SELECT * FROM {table}




Table ``client``
-----------------

..  code-block:: sql

    SELECT * FROM client

..  sqltable:: 
    :connection_string: sqlite:///bank.db
    :class: ocidbtable

    SELECT * FROM client


Table ``filiale``
-----------------

..  code-block:: sql

    SELECT * FROM filiale

..  sqltable:: 
    :connection_string: sqlite:///bank.db
    :class: ocidbtable

    SELECT * FROM filiale






Table ``compte``
-----------------

..  code-block:: sql

    SELECT * FROM compte

..  sqltable:: 
    :connection_string: sqlite:///bank.db
    :class: ocidbtable

    SELECT * FROM compte





Table ``possession``
-----------------

..  code-block:: sql

    SELECT * FROM possession

..  sqltable:: 
    :connection_string: sqlite:///bank.db
    :class: ocidbtable

    SELECT * FROM possession

Instructions SQL DDL
====================

..  literalinclude:: bank.sql
    :language: sql