CREATE TABLE `Bookings` (
  `CompositeKey` varchar(300) NOT NULL,
  `TimeKey` varchar(150) DEFAULT NULL,
  `UserEmail` varchar(300) DEFAULT NULL,
  `Phone` varchar(150) DEFAULT NULL,
  `Address` varchar(150) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `ConfirmationKey` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`CompositeKey`),
  UNIQUE KEY `CompositeKey_UNIQUE` (`CompositeKey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Completions` (
  `CompositeKey` varchar(300) NOT NULL,
  `LocationKey` varchar(300) DEFAULT NULL,
  `DateKey` varchar(300) DEFAULT NULL,
  `TimeKey` varchar(150) DEFAULT NULL,
  `UserEmail` varchar(300) DEFAULT NULL,
  `Phone` varchar(150) DEFAULT NULL,
  `Address` varchar(150) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `ConfirmationKey` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`CompositeKey`),
  UNIQUE KEY `CompositeKey_UNIQUE` (`CompositeKey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `Date`;
CREATE TABLE `Date` (
  `Key` varchar(300) NOT NULL,
  `Location` varchar(150) DEFAULT NULL,
  `Name` date DEFAULT NULL,
  PRIMARY KEY (`Key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `Datetime` (
  `Key` varchar(300) NOT NULL,
  `Date` varchar(150) DEFAULT NULL,
  `Name` varchar(150) DEFAULT NULL,
  `Times` time DEFAULT NULL,
  PRIMARY KEY (`Key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `Location` (
  `Key` varchar(300) NOT NULL,
  `Name` varchar(150) DEFAULT NULL,
  `Description` text,
  `Image` varchar(300) DEFAULT NULL,
  `Address` varchar(400) DEFAULT NULL,
  `LatLong` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`Key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `Preferences` (
  `Email` varchar(300) NOT NULL,
  `Search` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
