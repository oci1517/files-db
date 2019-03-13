..  Options coomplémentaire informatique : programmation documentation master file, created by
    sphinx-quickstart on Sat Sep  7 12:37:57 2013.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

#######################################
Module 6 : Persistance et bases de données
#######################################

.. comment::

   ..  admonition:: Référence et sources
      :class: danger

      Source : Ce cours est une adaptation de la section `Bases de données & SQL <http://www.tigerjython.ch/franz/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=datenbanken/datenbanken.inc.php>`_
      du magnifique ouvrage *Concepts de programmation* de Jarka Arnold, Tobias
      Kohn et Aegidius Plüss (www.tigerjython.fr).


.. only:: html

   .. admonition:: Version PDF de ce chapitre
      :class: tip

      *  :download:`files/oci-files-db.pdf`

   .. admonition:: Cours avec corrigés
      :class: info

      Une version de ce cours avec corrigés se trouve sous
      http://corrige.files-db.surge.sh/


..  toctree::
    :glob:
    :maxdepth: 1

    persistence-files/index
    csv/index
    xml/index

    intro/intro
    rel_mod/intro
    rel_mod/exos
    rel_algebra/intro
    rel_algebra/exos

    er_mod/chaj
    er_to_rel/notions
    sgbdr/sgbdr

    sql/ddl/create_table
    sql/ddl/insert

    sql/select/basic
    sql/select/basic-exos
    sql/select/learn-by-doing
    sql/select/advanced
    sql/select/advanced-exos
    sql/select/synthese-exos

    db-api/sqlite-api-theorie

    orm/index
    orm/optimization

    tools/index
