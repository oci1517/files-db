CREATE TABLE IF NOT EXISTS client (
  `client_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `nom` varchar(40) NOT NULL,
  `adresse` varchar(30) NOT NULL,
  `ville` varchar(30) NOT NULL,
  `canton` char(2) NOT NULL,
  `no_postal` char(4) NOT NULL
 
);

INSERT INTO `client` VALUES(1, 'Archambault', '2 Lindenstrasse', 'Zürich', 'ZH', '8000');
INSERT INTO `client` VALUES(2, 'Au plaisir de Lire', '10 route du Jura', 'Fribourg', 'FR', '1700');
INSERT INTO `client` VALUES(3, 'Librairie du Nouveau Monde', '35 rue des Acacias', 'Neuchâtel', 'NE', '2000');
INSERT INTO `client` VALUES(4, 'Librairie La Liberté', '1 avenue du Temple', 'Fribourg', 'FR', '1700');
INSERT INTO `client` VALUES(5, 'Globe Trotteur', '150 rue du Lac', 'Genève', 'GE', '1200');
INSERT INTO `client` VALUES(6, 'Arts Lettres et Technique', '20 Chaletweg', 'Basel', 'BS', '4000');
INSERT INTO `client` VALUES(7, 'Camelot', '7 Kramgasse', 'Luzern', 'LU', '6000');
INSERT INTO `client` VALUES(8, 'Livres et Jardins', '25 rue des Lilas', 'Bulle', 'FR', '1630');
INSERT INTO `client` VALUES(9, 'Librairie du Centre', '3 Place du Port', 'Nyon', 'GE', '1260');
INSERT INTO `client` VALUES(10, 'Papyrus', '40 rue de Carouge', 'Genève', 'GE', '1200');
INSERT INTO `client` VALUES(11, 'Mes Lectures Jeunesse', '12 rue des Sources', 'Genève', 'GE', '1200');
INSERT INTO `client` VALUES(12, 'Univers Bandes Dessinées', '52 avenue de la Gare', 'Lausanne', 'VD', '1000');
INSERT INTO `client` VALUES(13, 'Librairie Ulysse', '100 route de Meyrin', 'Genève', 'GE', '1200');
INSERT INTO `client` VALUES(14, 'Librairie de l''Université', '6 Haldenstrasse', 'Berne', 'BE', '3000');
INSERT INTO `client` VALUES(15, 'Le Bouquiniste', '1 place de Bel-Air', 'Genève', 'GE', '1200');

CREATE TABLE `commande` (
  `commande_id` INTEGER PRIMARY KEY AUTOINCREMENT ,
  `date` date NOT NULL,
  `client_id` int(11) NOT NULL,
  
  -- contraintes de table
  FOREIGN KEY (`client_id`) REFERENCES `Client` (`cliend_id`) ON DELETE NO ACTION
);

INSERT INTO `commande` VALUES(1001, '2011-08-21', 1);
INSERT INTO `commande` VALUES(1002, '2011-08-21', 8);
INSERT INTO `commande` VALUES(1003, '2011-08-22', 15);
INSERT INTO `commande` VALUES(1004, '2011-08-22', 5);
INSERT INTO `commande` VALUES(1005, '2011-08-24', 3);
INSERT INTO `commande` VALUES(1006, '2011-08-24', 2);
INSERT INTO `commande` VALUES(1007, '2011-08-27', 11);
INSERT INTO `commande` VALUES(1008, '2011-08-21', 12);
INSERT INTO `commande` VALUES(1009, '2011-09-05', 4);
INSERT INTO `commande` VALUES(1010, '2011-09-05', 1);

CREATE TABLE `ligne_commande` (
  `commande_id` INTEGER NOT NULL,
  `produit_id` INTEGER NOT NULL,
  `quantite` INTEGER NOT NULL,
  
  -- contraintes de table
  PRIMARY KEY (`commande_id`,`produit_id`),
  
  -- intégrité référentielle
  FOREIGN KEY (`commande_id`) REFERENCES `commande` (`commande_id`) ON DELETE CASCADE,
  FOREIGN KEY (`produit_id`) REFERENCES `produit` (`produit_id`) ON DELETE NO ACTION
);

INSERT INTO `ligne_commande` VALUES(1001, 100, 20);
INSERT INTO `ligne_commande` VALUES(1001, 300, 5);
INSERT INTO `ligne_commande` VALUES(1001, 400, 10);
INSERT INTO `ligne_commande` VALUES(1002, 300, 2);
INSERT INTO `ligne_commande` VALUES(1003, 300, 10);
INSERT INTO `ligne_commande` VALUES(1004, 300, 30);
INSERT INTO `ligne_commande` VALUES(1004, 600, 20);
INSERT INTO `ligne_commande` VALUES(1004, 800, 20);
INSERT INTO `ligne_commande` VALUES(1005, 400, 40);
INSERT INTO `ligne_commande` VALUES(1006, 400, 10);
INSERT INTO `ligne_commande` VALUES(1006, 500, 20);
INSERT INTO `ligne_commande` VALUES(1006, 700, 20);
INSERT INTO `ligne_commande` VALUES(1007, 100, 30);
INSERT INTO `ligne_commande` VALUES(1007, 200, 20);
INSERT INTO `ligne_commande` VALUES(1008, 300, 8);
INSERT INTO `ligne_commande` VALUES(1008, 800, 30);
INSERT INTO `ligne_commande` VALUES(1009, 400, 20);
INSERT INTO `ligne_commande` VALUES(1009, 700, 30);
INSERT INTO `ligne_commande` VALUES(1010, 800, 100);

CREATE TABLE `produit` (
  `produit_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `description` varchar(60) NOT NULL,
  `reliure` varchar(30) NOT NULL,
  `prix_unitaire` FLOAT NOT NULL
);

INSERT INTO `produit` VALUES(100, 'Le guide des vins 2012', 'Cartonné', 50);
INSERT INTO `produit` VALUES(200, 'Dieux du stade', 'Cartonné', 100);
INSERT INTO `produit` VALUES(300, 'Rupture de contrat', 'Broché', 10);
INSERT INTO `produit` VALUES(400, 'Pars vite et reviens tard', 'Broché', 12);
INSERT INTO `produit` VALUES(500, 'Panique au collège', 'Broché', 7);
INSERT INTO `produit` VALUES(600, 'Marketing management', 'Spirales', 120);
INSERT INTO `produit` VALUES(700, 'L''art de la guerre', 'Cartonné', 12);
INSERT INTO `produit` VALUES(800, 'Excel pour le business et la finance', 'Spirales', 75);
INSERT INTO `produit` VALUES(900, '10 ans de leçon de séduction', 'Cartonné', 60);
INSERT INTO `produit` VALUES(1000, 'Autant en emporte le vent', 'Cuir', 150);