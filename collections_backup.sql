-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: collections
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `collector_notes`
--

DROP TABLE IF EXISTS `collector_notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collector_notes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `note` text NOT NULL,
  `collector_id` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `transaction_id` int DEFAULT NULL,
  `payment_plan_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `collector_id` (`collector_id`),
  KEY `fk_transaction` (`transaction_id`),
  KEY `fk_payment_plan` (`payment_plan_id`),
  CONSTRAINT `collector_notes_ibfk_1` FOREIGN KEY (`collector_id`) REFERENCES `collectors` (`id`),
  CONSTRAINT `fk_payment_plan` FOREIGN KEY (`payment_plan_id`) REFERENCES `payment_plans` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_transaction` FOREIGN KEY (`transaction_id`) REFERENCES `customer_transactions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collector_notes`
--

LOCK TABLES `collector_notes` WRITE;
/*!40000 ALTER TABLE `collector_notes` DISABLE KEYS */;
INSERT INTO `collector_notes` VALUES (1,'This is a note for John.',1,'2025-01-07 21:14:16','2025-01-07 21:14:16',NULL,NULL),(3,'First note for Alice',1,'2025-01-07 21:16:40','2025-01-07 21:16:40',NULL,NULL),(4,'First note for Bob',2,'2025-01-07 21:16:40','2025-01-07 21:16:40',NULL,NULL),(5,'First note for Charlie',3,'2025-01-07 21:16:40','2025-01-07 21:16:40',NULL,NULL),(6,'Testing App',NULL,'2025-01-07 22:05:29','2025-01-07 22:05:29',2,2);
/*!40000 ALTER TABLE `collector_notes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collectors`
--

DROP TABLE IF EXISTS `collectors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collectors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collectors`
--

LOCK TABLES `collectors` WRITE;
/*!40000 ALTER TABLE `collectors` DISABLE KEYS */;
INSERT INTO `collectors` VALUES (1,'John Doe','john.doe@example.com','2025-01-07 21:14:10'),(2,'Alice Johnson','alice.johnson@example.com','2025-01-07 21:16:17'),(3,'Bob Smith','bob.smith@example.com','2025-01-07 21:16:17'),(4,'Charlie Brown','charlie.brown@example.com','2025-01-07 21:16:17');
/*!40000 ALTER TABLE `collectors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_transactions`
--

DROP TABLE IF EXISTS `customer_transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_transactions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(255) NOT NULL,
  `transaction_date` date DEFAULT NULL,
  `amount` decimal(10,2) NOT NULL,
  `collector_id` int DEFAULT NULL,
  `transaction_time` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `collector_id` (`collector_id`),
  CONSTRAINT `customer_transactions_ibfk_1` FOREIGN KEY (`collector_id`) REFERENCES `collectors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_transactions`
--

LOCK TABLES `customer_transactions` WRITE;
/*!40000 ALTER TABLE `customer_transactions` DISABLE KEYS */;
INSERT INTO `customer_transactions` VALUES (1,'Emily Davis','2025-01-07',150.00,1,'21:17:55'),(2,'Frank Moore','2025-01-07',200.00,2,'21:17:55'),(3,'Grace Lee','2025-01-07',250.00,3,'21:17:55');
/*!40000 ALTER TABLE `customer_transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_plans`
--

DROP TABLE IF EXISTS `payment_plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_plans` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plan_name` varchar(255) NOT NULL,
  `duration` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_plans`
--

LOCK TABLES `payment_plans` WRITE;
/*!40000 ALTER TABLE `payment_plans` DISABLE KEYS */;
INSERT INTO `payment_plans` VALUES (1,'Basic Plan',12,199.99,'2025-01-01','2026-01-01'),(2,'Premium Plan',24,299.99,'2025-02-01','2027-02-01'),(3,'Enterprise Plan',36,499.99,'2025-03-01','2028-03-01');
/*!40000 ALTER TABLE `payment_plans` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-07 22:49:11
