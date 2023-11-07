-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 07 nov. 2023 à 00:56
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `oop-project`
--

-- --------------------------------------------------------

--
-- Structure de la table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `CustomerID` int NOT NULL,
  `FirstName` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LastName` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Email` text NOT NULL,
  `Phone` int NOT NULL,
  `UserName` text NOT NULL,
  `Password` text NOT NULL,
  `AdminOrNot` tinyint(1) NOT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `customer`
--

INSERT INTO `customer` (`CustomerID`, `FirstName`, `LastName`, `Email`, `Phone`, `UserName`, `Password`, `AdminOrNot`) VALUES
(1, 'Mathis', 'GRAS', 'test@gmail.com', 101010101, 'Poule', 'root', 1),
(2, 'Victor', 'LAMBERT', 'jsp@gmail.com', 101010102, 'vico', 'proot', 0);

-- --------------------------------------------------------

--
-- Structure de la table `flight`
--

DROP TABLE IF EXISTS `flight`;
CREATE TABLE IF NOT EXISTS `flight` (
  `FlightID` int NOT NULL,
  `FlightNumber` text NOT NULL,
  `Departure` text NOT NULL,
  `DepartureTime` datetime NOT NULL,
  `Arrival` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ArrivalTime` datetime NOT NULL,
  `Price` float NOT NULL,
  `Discount` float NOT NULL,
  `SeatsAvailable` int NOT NULL,
  `Seats` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `flight`
--

INSERT INTO `flight` (`FlightID`, `FlightNumber`, `Departure`, `DepartureTime`, `Arrival`, `ArrivalTime`, `Price`, `Discount`, `SeatsAvailable`, `Seats`) VALUES
(1, 'AA101', 'New York', '2023-11-15 08:00:00', 'Los Angeles', '2023-11-15 10:30:00', 250, 0.05, 150, 150),
(2, 'UA202', 'Chicago', '2023-11-16 10:30:00', 'Houston', '2023-11-16 13:00:00', 200, 0.1, 120, 120),
(3, 'DL303', 'San Francisco', '2023-11-17 12:00:00', 'Miami', '2023-11-17 16:30:00', 300, 0.05, 180, 180),
(4, 'AA150', 'Boston', '2023-12-01 09:30:00', 'Seattle', '2023-12-01 12:00:00', 220, 0.1, 200, 200),
(5, 'UA250', 'Dallas', '2023-12-02 11:15:00', 'Denver', '2023-12-02 13:45:00', 180, 0.05, 150, 150),
(6, 'DL350', 'Las Vegas', '2023-12-03 14:45:00', 'Orlando', '2023-12-03 18:15:00', 320, 0.1, 100, 100);

-- --------------------------------------------------------

--
-- Structure de la table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
CREATE TABLE IF NOT EXISTS `reservations` (
  `ReservationID` int NOT NULL,
  `ReservationDate` datetime NOT NULL,
  `NumTicket` int NOT NULL,
  `FlightID` int NOT NULL,
  `CustomerID` int NOT NULL,
  PRIMARY KEY (`ReservationID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `reservations`
--

INSERT INTO `reservations` (`ReservationID`, `ReservationDate`, `NumTicket`, `FlightID`, `CustomerID`) VALUES
(1, '2023-11-06 14:30:00', 0, 1, 1001),
(2, '2023-11-07 15:45:00', 0, 2, 1002),
(3, '2023-11-08 10:15:00', 0, 3, 1003),
(4, '2023-11-09 09:00:00', 0, 4, 1004),
(5, '2023-11-10 11:30:00', 0, 5, 1005);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
