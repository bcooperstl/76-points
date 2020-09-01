
-- game_locations table - basically for home vs away.

CREATE TABLE `game_locations` (
  `game_location_id` char(1) NOT NULL,
  `game_location` varchar(8) NOT NULL,
  PRIMARY KEY (`game_location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `game_locations` VALUES ('A','Away'),('H','Home'),('N','Neutral');

-- game_types - for regular season vs post season.

CREATE TABLE `game_types` (
  `game_type_id` char(1) NOT NULL,
  `game_type` varchar(16) NOT NULL,
  PRIMARY KEY (`game_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `game_types` VALUES ('R','Regular Season'),('P','Postseason');

-- result_types - for the different affects around 76 points. See the descriptions of each entry

CREATE TABLE `result_types` (
  `result_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(6) NOT NULL,
  `description` varchar(256) DEFAULT NULL,
  `start_score` int(11) DEFAULT NULL,
  `end_score` int(11) DEFAULT NULL,
  `is_76` tinyint(4) NOT NULL,
  PRIMARY KEY (`result_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `result_types` VALUES (1,'73-76','3-point shot; score goes 73 to 76',73,76,1);
INSERT INTO `result_types` VALUES (2,'74-77','3-point shot; score goes 74 to 77',74,77,0);
INSERT INTO `result_types` VALUES (3,'75-78','3-point shot; score goes 75 to 78',75,78,0);
INSERT INTO `result_types` VALUES (4,'74-76','2-point shot; score goes 74 to 76',74,76,1);
INSERT INTO `result_types` VALUES (5,'75-77','2-point shot; score goes 75 to 77',75,77,0);
INSERT INTO `result_types` VALUES (6,'75-76','Free throw; score goes 75 to 76',75,76,1);
INSERT INTO `result_types` VALUES (7,'Under','Team did not score 76 points in the game',NULL,NULL,0);

-- the games and their results

CREATE TABLE `games` (
  `game_id` int(11) NOT NULL AUTO_INCREMENT,
  `season_start_year` int(11) NOT NULL,
  `game_type_id` char(1) NOT NULL,
  `game_date` date NOT NULL,
  `game_location_id` char(1) NOT NULL,
  `opponent` varchar(4) NOT NULL,
  `our_final_score` int(11) NOT NULL,
  `opponent_final_score` int(11) NOT NULL,
  `is_box_score_downloaded` tinyint(4) NOT NULL DEFAULT '0',
  `is_box_score_processed` tinyint(4) NOT NULL DEFAULT '0',
  `result_type_id` int(11) DEFAULT NULL,
  `result_comments` varchar(256) DEFAULT NULL,
  `box_score_filename` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

