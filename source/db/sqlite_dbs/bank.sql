CREATE TABLE IF NOT EXISTS client
( 
    -- définition des colonnes (champs)
    no_client INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(40) NOT NULL,
    prenom VARCHAR(40) NOT NULL

    -- pas de contrainte de table
);


CREATE TABLE IF NOT EXISTS filiale
( 
    -- définition des colonnes (champs)
    no_filiale INTEGER PRIMARY KEY AUTOINCREMENT,
    ville VARCHAR(20) NOT NULL,
    no INTEGER NOT NULL DEFAULT 1

    -- pas de contrainte de table
);


CREATE TABLE IF NOT EXISTS compte
( 
    -- définition des colonnes (champs)
    no_compte INTEGER PRIMARY KEY AUTOINCREMENT,
    montant DECIMAL(7,2) NOT NULL DEFAULT 0,
    date_acces DATETIME NULL,
    no_filiale INTEGER NOT NULL,

    -- contrainte de table
    FOREIGN KEY (no_filiale) REFERENCES filiale (no_filiale)
);


CREATE TABLE IF NOT EXISTS possession
( 
    no_compte INTEGER NOT NULL,
    no_client INTEGER NOT NULL,

    -- Clé primaire composée des champs (no_compte, no_client)
    -- contrainte de table
    PRIMARY KEY(no_compte, no_client)

    -- Contraintes d'intégrité référentielle
    FOREIGN KEY (no_compte) REFERENCES compte (no_compte)
        -- Si un compte est effacé, il faut également effacé les 
        -- références à ce compte
        ON DELETE CASCADE
    FOREIGN KEY (no_client) REFERENCES compte (no_client)
        -- Il ne faut pas pouvoir effacer un client s'il possède
        -- encore des comptes en banque dans la table ``compte``
        ON DELETE NO ACTION
);

INSERT INTO client (no_client, nom, prenom) VALUES (1, 'Turing', 'Alan');
INSERT INTO client (no_client, nom, prenom) VALUES (2, 'Honegger', 'Arthur');
INSERT INTO client (no_client, nom, prenom) VALUES (3, 'Euler', 'Leonhard');
INSERT INTO client (no_client, nom, prenom) VALUES (4, 'Riemann', 'Berhard');
INSERT INTO client (no_client, nom, prenom) VALUES (5, 'von Neuman', 'John');

INSERT INTO filiale (ville, no, no_filiale) VALUES ('Bulle', 1, 1);
INSERT INTO filiale (ville, no, no_filiale) VALUES ('Fribourg', 1, 2);
INSERT INTO filiale (ville, no, no_filiale) VALUES ('Lausanne', 1, 3);
INSERT INTO filiale (ville, no, no_filiale) VALUES ('Lausanne', 2, 4);
INSERT INTO filiale (ville, no, no_filiale) VALUES ('Zurich', 1, 5);
INSERT INTO filiale (ville, no, no_filiale) VALUES ('Zurich', 2, 6);
INSERT INTO filiale (ville, no, no_filiale) VALUES ('Zurich', 3, 7);

INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (1, 500, '01.01.2010', 1);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (2, 500, '01.01.2010', 1);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (3, 700, '03.04.2010', 4);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (4, 8000, '05.07.2010', 3);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (5, 6000, '05.10.2010', 1);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (6, 4000, '23.02.2010', 1);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (7, 10000, '15.04.2010', 2);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (8, 2300, '12.10.2010', 3);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (9, 5600, '23.06.2010', 2);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (10, 2300, '11.10.2010', 6);
INSERT INTO compte (no_compte, montant, date_acces, no_filiale) VALUES (11, 5400, '01.01.2010', 4);

INSERT INTO possession (no_client, no_compte) VALUES (1, 1);
INSERT INTO possession (no_client, no_compte) VALUES (2, 1);
INSERT INTO possession (no_client, no_compte) VALUES (1, 2);
INSERT INTO possession (no_client, no_compte) VALUES (2, 3);
INSERT INTO possession (no_client, no_compte) VALUES (1, 4);
INSERT INTO possession (no_client, no_compte) VALUES (4, 5);
INSERT INTO possession (no_client, no_compte) VALUES (2, 6);
INSERT INTO possession (no_client, no_compte) VALUES (2, 7);
INSERT INTO possession (no_client, no_compte) VALUES (1, 8);
INSERT INTO possession (no_client, no_compte) VALUES (4, 9);
INSERT INTO possession (no_client, no_compte) VALUES (1, 10);
INSERT INTO possession (no_client, no_compte) VALUES (2, 11);
