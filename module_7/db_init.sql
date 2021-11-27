DROP USER IF EXISTS 'pysports_root'@'localhost:3306/pysports';
CREATE USER 'pysports_root'@'localhost:3306/pysports'IDENTIFIED WITH mysql_native_password BY 'Finnissee1!';
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_root'@'localhost:3306/pysports';
FLUSH PRIVILEGES;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

CREATE TABLE team (
team_id       INT             NOT NULL            AUTO_INCREMENT,
team_name     VARCHAR(75)     NOT NULL,
mascot        VARCHAR(75)     NOT NULL,
PRIMARY KEY (team_id)
);

CREATE TABLE player (
player_id            INT            NOT NULL             AUTO_INCREMENT,
first_name           VARCHAR(75)    NOT NULL,
last_name            VARCHAR(75)    NOT NULL,
team_id              INT            NOT NULL,
PRIMARY KEY(player_id),
CONSTRAINT fk_team
FOREIGN KEY(team_id)
REFERENCES team(team_id)
);

INSERT INTO team(team_id, team_name,mascot)
VALUES('229', 'VALDOSTA_WILDCATS', 'WILDCAT')

INSERT INTO team(team_id, team_name,mascot)
VALUES('230', 'LOWNDES_VIKINGS', 'VIKINGS')

INSERT INTO player(player_id, first_name, last_name, team_id)
VALUES('14', 'TREVONE', 'BOYKIN', '229')
INSERT INTO player(player_id, first_name, last_name, team_id)
VALUES('15', 'DEVONTA', 'SMITH', '229')
INSERT INTO player(player_id, first_name, last_name, team_id)
VALUES('16', 'DERRICK', 'HENRY', '229')

INSERT INTO player(player_id, first_name, last_name, team_id)
VALUES('17', 'BO', 'NIX', '230')
INSERT INTO player(player_id, first_name, last_name, team_id)
VALUES('18', 'CHRIS', 'OLAVE', '230')
INSERT INTO player(player_id, first_name, last_name, team_id)
VALUES('19', 'BIJAN', 'ROBINSON', '230')

SELECT team_id FROM team WHERE team_name = 'VALDOSTA_WILDACTS'
SELECT team_id FROM team WHERE team_name = 'LOWNDES_VIKINGS'