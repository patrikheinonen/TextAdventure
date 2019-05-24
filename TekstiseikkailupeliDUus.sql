DROP DATABASE IF EXISTS tekstiseikkailuTEST;

#luodaan uusi, tyhjÃƒÂ¤ demoquest-tietotaknta

CREATE DATABASE tekstiseikkailuTEST;
USE tekstiseikkailuTEST;




CREATE TABLE LOCATION (
	Id VARCHAR(10) NOT NULL,
	Description VARCHAR(120),
	Details VARCHAR(1000),
	PRIMARY KEY (Id)
) ENGINE=InnoDB;

CREATE TABLE PLAYER (
	Id VARCHAR(10) NOT NULL,
	Location VARCHAR(10) NOT NULL,
	PRIMARY KEY (Id),
	FOREIGN KEY (Location) REFERENCES LOCATION(Id)
) ENGINE=InnoDB;

CREATE TABLE OBJECT (
	Id VARCHAR(30) NOT NULL,
	Description VARCHAR(40),
	Refname VARCHAR(40),
	Details VARCHAR(1000),
	Location VARCHAR(10),
	Available BOOLEAN,
	Takeable BOOLEAN,
	PlayerId VARCHAR(10),
	Lvl INT(1),
	PRIMARY KEY (Id),
	FOREIGN KEY (Location) REFERENCES LOCATION(Id),
	FOREIGN KEY (PlayerId) REFERENCES PLAYER(Id)
) ENGINE=InnoDB;

CREATE TABLE ENEMIES (
	Id VARCHAR(30) NOT NULL,
	Description VARCHAR(1000),
	Refname VARCHAR(40),
	Location VARCHAR(10),
	Relation VARCHAR (10),
	Lvl INT(1),
	PRIMARY KEY (Id),
	FOREIGN KEY (Location) REFERENCES LOCATION (Id)
) ENGINE=InnoDB;

CREATE TABLE DIRECTION (
	Id VARCHAR(10) NOT NULL,
	Description VARCHAR(40),
	PRIMARY KEY (Id)
) ENGINE=InnoDB;

CREATE TABLE PASSAGE (
	Id INT NOT NULL,
	Source VARCHAR(10),
	Destination VARCHAR(10),
	Direction VARCHAR(10),
	Locked BOOLEAN,
	PRIMARY KEY (Id),
	FOREIGN KEY (Source) REFERENCES LOCATION(Id),
	FOREIGN KEY (Destination) REFERENCES LOCATION(Id),
	FOREIGN KEY (Direction) REFERENCES DIRECTION(Id)
) ENGINE=InnoDB;


INSERT INTO LOCATION VALUES ('Shelter1', 'A Small tent', 'Smells weird. There is some torches behind Lisa. They must be usefull in here.');
INSERT INTO LOCATION VALUES ('Shelter2', 'A Large tent', 'Looks comfortable. Steve has a large collection of various items.');
INSERT INTO LOCATION VALUES ('Camparea', 'Camp area', 'There are some survivors! Some of the people are staring at you, but they are more focused on doing their own things. Maybe there is someone who likes to talk?');
INSERT INTO LOCATION VALUES ('Fdeck', 'Flight deck', 'You look around and notice that everything is broken.');
INSERT INTO LOCATION VALUES ('planepiece', 'My crashed plane', 'Looks like I am the only one	who survived the crash. Maybe I could find something useful?');
INSERT INTO LOCATION VALUES ('MountRoot', 'A rocky mountain root', 'Theres large rocks here, but you found nothing interesting.');
INSERT INTO LOCATION VALUES ('MRL',  'Mountain root and a lake', 'Beautiful lake with fresh water.');
INSERT INTO LOCATION VALUES ('MountRoot2', 'A Steep mountain root', 'Thats a very steep mountain theres no way to climb it!');
INSERT INTO LOCATION VALUES ('JngPlane', 'An old WW II warplane', 'That looks amazing! Maybe I could find a use for some of the planeparts?');
INSERT INTO LOCATION VALUES ('Jng1',  'Jungle with swamps', 'A smelly swamp in the middle of a jungle?');
INSERT INTO LOCATION VALUES ('Jng2', 'Jungle with thick vegetation', 'Its hard to move around here.');
INSERT INTO LOCATION VALUES ('AbaCmp', 'A abandoned camp', 'It looks like this place was abandoned recently ... There is a lot of broken stuff in here.');
INSERT INTO LOCATION VALUES ('Grave', 'A graveyard', 'Its very scary in here, the graves are in bad shape and the sunlight is blocked by trees.');
INSERT INTO LOCATION VALUES ('StartBch','Awakening beach', 'My plane crash-landed and I woke up here.');
INSERT INTO LOCATION VALUES ('Bch', 'More beach', 'Sand, sand and sand. There is nothing interesting, but I can see a shipwreck far in the south.');
INSERT INTO LOCATION VALUES ('BchWs',  'Beach and a shipwreck', 'When you examine the ship you see that it has been fixed. It is possible to escape from the island! But why is it still here?');
INSERT INTO LOCATION VALUES ('Jng3',  'Rocky jungle', 'Huge rocky clifs.');
INSERT INTO LOCATION VALUES ('Cave',  'A cave!', 'Why are there locked doors?');
INSERT INTO LOCATION VALUES ('Tomb', 'A tomb?', 'Who is buried in here? Oh wait! There is an armour and a sword hanging from the roof! How could i get them down?');
INSERT INTO LOCATION VALUES ('Freedom', 'Freedom', 'The island behind me looks smaller and smaller. ');
INSERT INTO LOCATION VALUES ('Sea', 'Ship', 'The ship that the survivors repaired. Wood everywhere.');
INSERT INTO LOCATION VALUES ('Dead',  'You died!', 'I do not like this company...');


INSERT INTO PLAYER VALUES('Player','StartBch');


INSERT INTO DIRECTION VALUES ('n', 'North');
INSERT INTO DIRECTION VALUES ('s', 'South');
INSERT INTO DIRECTION VALUES ('e', 'East');
INSERT INTO DIRECTION VALUES ('w', 'West');
INSERT INTO DIRECTION VALUES ('sw', 'Southwest');
INSERT INTO DIRECTION VALUES ('ne', 'Northeast');


INSERT INTO PASSAGE VALUES (1, 'Shelter1', 'Camparea', 's', FALSE);
INSERT INTO PASSAGE VALUES (2, 'Camparea', 'Shelter1','n',FALSE);
INSERT INTO PASSAGE VALUES (3, 'Shelter2', 'Camparea', 'w', FALSE);
INSERT INTO PASSAGE VALUES (4, 'Camparea', 'Shelter2', 'e', FALSE);
INSERT INTO PASSAGE VALUES (5, 'Camparea', 'planepiece', 's', FALSE);
INSERT INTO PASSAGE VALUES (6, 'planepiece', 'Camparea', 'n', FALSE);
INSERT INTO PASSAGE VALUES (7, 'planepiece', 'Fdeck', 'ne', FALSE);
INSERT INTO PASSAGE VALUES (8, 'Fdeck', 'planepiece', 's', FALSE);
INSERT INTO PASSAGE VALUES (9, 'planepiece', 'MountRoot', 'w', FALSE);
INSERT INTO PASSAGE VALUES (10, 'MountRoot', 'planepiece', 'e', FALSE);
INSERT INTO PASSAGE VALUES (11, 'planepiece', 'Jng2', 'e', FALSE);
INSERT INTO PASSAGE VALUES (12, 'Jng2', 'planepiece', 'w', FALSE);
INSERT INTO PASSAGE VALUES (13, 'planepiece', 'Jng1', 's', FALSE);
INSERT INTO PASSAGE VALUES (14, 'Jng1', 'planepiece', 'n', FALSE);
INSERT INTO PASSAGE VALUES (15, 'MountRoot', 'MRL', 's', FALSE);
INSERT INTO PASSAGE VALUES (16, 'MRL', 'MountRoot', 'n', FALSE);
INSERT INTO PASSAGE VALUES (17, 'MRL', 'MountRoot2', 's', FALSE);
INSERT INTO PASSAGE VALUES (18, 'MountRoot2', 'MRL', 'n', FALSE);
INSERT INTO PASSAGE VALUES (19, 'MountRoot2', 'JngPlane', 'e', FALSE);
INSERT INTO PASSAGE VALUES (20, 'JngPlane', 'MountRoot2', 'w', FALSE);
INSERT INTO PASSAGE VALUES (21, 'JngPlane', 'Jng1', 'n', FALSE);
INSERT INTO PASSAGE VALUES (22, 'Jng1', 'JngPlane', 's', FALSE);
INSERT INTO PASSAGE VALUES (23, 'JngPlane', 'Jng3', 's', FALSE);
INSERT INTO PASSAGE VALUES (24, 'Jng3', 'JngPlane', 'n', FALSE);
INSERT INTO PASSAGE VALUES (25, 'JngPlane', 'Grave', 'e', FALSE);
INSERT INTO PASSAGE VALUES (26, 'Grave', 'JngPlane', 'w', FALSE);
INSERT INTO PASSAGE VALUES (27, 'Jng1', 'AbaCmp', 'e', FALSE);
INSERT INTO PASSAGE VALUES (28, 'AbaCmp', 'Jng1', 'w', FALSE);
INSERT INTO PASSAGE VALUES (29, 'Jng2', 'AbaCmp', 's', FALSE);
INSERT INTO PASSAGE VALUES (30, 'AbaCmp', 'Jng2', 'n', FALSE);
INSERT INTO PASSAGE VALUES (31, 'Jng2', 'StartBch', 'e', FALSE);
INSERT INTO PASSAGE VALUES (32, 'StartBch', 'Jng2', 'w', FALSE);
INSERT INTO PASSAGE VALUES (33, 'AbaCmp', 'Grave', 's', FALSE);
INSERT INTO PASSAGE VALUES (34, 'Grave', 'AbaCmp', 'n', FALSE);
INSERT INTO PASSAGE VALUES (35, 'AbaCmp', 'Bch', 'e', FALSE);
INSERT INTO PASSAGE VALUES (36, 'Bch', 'AbaCmp', 'w', FALSE);
INSERT INTO PASSAGE VALUES (37, 'Grave', 'Jng3', 's', FALSE);
INSERT INTO PASSAGE VALUES (38, 'Jng3', 'Grave', 'ne', FALSE);
INSERT INTO PASSAGE VALUES (39, 'Grave', 'BchWs', 'e', FALSE);
INSERT INTO PASSAGE VALUES (40, 'BchWs', 'Grave', 'w', FALSE);
INSERT INTO PASSAGE VALUES (41, 'Jng3', 'BchWs', 'e', FALSE);
INSERT INTO PASSAGE VALUES (42, 'BchWs', 'Jng3', 'sw', FALSE);
INSERT INTO PASSAGE VALUES (43, 'Jng3', 'Cave', 'w', TRUE);
INSERT INTO PASSAGE VALUES (44, 'Cave', 'Jng3', 'e', FALSE);
INSERT INTO PASSAGE VALUES (45, 'Cave', 'Tomb', 'w', TRUE);
INSERT INTO PASSAGE VALUES (46, 'Tomb', 'Cave', 'e', FALSE);
INSERT INTO PASSAGE VALUES (47, 'BchWs', 'Bch', 'n', FALSE);
INSERT INTO PASSAGE VALUES (48, 'Bch', 'BchWs', 's', FALSE);
INSERT INTO PASSAGE VALUES (49, 'StartBch', 'Bch', 's', FALSE);
INSERT INTO PASSAGE VALUES (50, 'Bch', 'StartBch', 'n', FALSE);
INSERT INTO PASSAGE VALUES (51, 'BchWs', 'Sea', 'e', FALSE);
INSERT INTO PASSAGE VALUES (52, 'Jng1', 'MRL', 'w', FALSE);
INSERT INTO PASSAGE VALUES (53, 'MRL', 'Jng1', 'e', FALSE);
INSERT INTO PASSAGE VALUES (54, 'Sea', 'Freedom', 'e', FALSE);




#INSERT INTO OBJECT VALUES(Id, dESCRIPTION, refname, details, location, available, takeable, plaeyrid, level);
INSERT INTO OBJECT VALUES('WSTICK', 'Looks like a stick., smells funny.', 'WoodStick', 'fell from a tree', 'Jng2', TRUE, TRUE, NULL,0);
INSERT INTO OBJECT VALUES('RSWORD', 'Its a rusty sword.', 'RustySword', 'It is very dull and rusty. Looks like it has been here for a while.', 'BchWs', TRUE, TRUE, NULL, 1);
INSERT INTO OBJECT VALUES('SSWORD', 'Its a steel sword.', 'SteelSword', 'A proper sword, looks like it is very sharp.', 'Camparea', TRUE, TRUE, NULL, 2);
INSERT INTO OBJECT VALUES('SOLSWORD', 'This must be a Sword of Light.', 'LightSword', 'A mythical sword, looks like it fell from an angel.', 'Grave', TRUE, TRUE, NULL, 3);
INSERT INTO OBJECT VALUES('MSWORD', 'A powerfull sword.', 'MasterSword', 'A godlike sword, crafted by god himself.', 'Tomb', TRUE, FALSE, NULL, 4);
INSERT INTO OBJECT VALUES('MARMOUR', 'A powerfull armour.', 'Armour', 'A godlike armor, crafted by god himself.', 'Tomb', TRUE, FALSE, NULL, 0);
INSERT INTO OBJECT VALUES('GKEY', 'A green key.', 'GreenKey', 'Shines with green light.', 'Jng2', FALSE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('BKEY', 'A blue key.', 'BlueKey', 'Shines with blue light.', 'MRL', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('RKEY', 'A red key.', 'RedKey', 'Shines with red light.', 'Shelter2', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('SHCOG', 'Are they serious?', 'SircularSaw', 'In my opinion it looks more like a sharp cogwheel...', 'Camparea', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('SCOG', 'A small Cog Wheel.', 'SmallCogWheel', 'This must be usefull in somewhere.', 'JngPlane', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('LCOG', 'A large cog wheel.', 'LargeCogWheel', 'This must be usefull in somewhere.', 'AbaCmp', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('COCO', 'Juicy coconut. ', 'Coconut', 'It does look good.', 'StartBch', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('ROPE', 'Short peace of rope.', 'Rope', 'It is not old neither strong.', 'AbaCmp', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('LIGHTER', 'Working lighter.', 'Lighter', 'Who took a lighter into a plane?', 'Fdeck', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('TORCH', 'Torch.', 'Torch', 'I can lighten a place with this', 'Shelter1', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('ROCK', 'Stone.', 'Stone', 'Maybe I could throw it?', 'Tomb', TRUE, TRUE, NULL, 0);
INSERT INTO OBJECT VALUES('CAVEENTR', 'Entrance to the cave.', 'cavehole', 'Its so dark in there. It is too dangereous to go in.', 'Jng3', TRUE, FALSE, NULL, 0);
INSERT INTO OBJECT VALUES('STONEDOOR', 'Stonedoor.', 'stonedoor', 'it looks like some kind of spinning objects are missing from the door.', 'Cave', TRUE, FALSE, NULL, 0);
INSERT INTO OBJECT VALUES('TOMBENTR', 'Entrance to the tomb.', 'Tombdoor', 'There is a keyhole. Above the keyhole theres a riddle that goes: To enter you must posses the colour of life.', 'Cave', FALSE, FALSE, NULL, 0);

INSERT INTO ENEMIES VALUES('Spider1', 'A giant spider!I have never seen anything like that!','giantspider','Jng1', 'Enemy', 2);
INSERT INTO ENEMIES VALUES('Spider2', 'It is a massive! I have never seen anything like that!','giantspider','AbaCmp', 'Enemy', 2);
INSERT INTO ENEMIES VALUES('Spider3', 'It is a massive! I have never seen anything like that!','giantspider','Grave', 'Enemy', 2);
INSERT INTO ENEMIES VALUES('Spider4', 'A giant spider! I have never seen anything like that!','giantspider','JngPlane', 'Enemy', 2);
INSERT INTO ENEMIES VALUES('Troll1', 'Am I dreaming? That cant be real!','troll','Tomb', 'Enemy', 3);
INSERT INTO ENEMIES VALUES('Troll2', 'Am I dreaming? That cant be real!','troll','MRL', 'Enemy', 3);
INSERT INTO ENEMIES VALUES('Troll3', 'It looks very angry!','troll','Jng3', 'Enemy', 3);
INSERT INTO ENEMIES VALUES('Troll4', 'It looks very angry!','troll','Cave', 'Enemy', 3);
INSERT INTO ENEMIES VALUES('Mainboss', 'It must be a monster from darkest nightmares!','demon','Sea', 'Enemy', 4);
INSERT INTO ENEMIES VALUES('Marco', 'He is a seasoned adventurer stuck in the island like you.','marco','Camparea', 'Neutral', 1);
INSERT INTO ENEMIES VALUES('Lisa', 'She is a middle aged woman who knows how to create torches.','lisa','Shelter1', 'Neutral', 1);
INSERT INTO ENEMIES VALUES('Steve', 'He likes to lay in his bed and relax. ','steve','Shelter2', 'Neutral', 1);










