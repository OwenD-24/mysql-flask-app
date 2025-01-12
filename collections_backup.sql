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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collector_notes`
--

LOCK TABLES `collector_notes` WRITE;
/*!40000 ALTER TABLE `collector_notes` DISABLE KEYS */;
INSERT INTO `collector_notes` VALUES (13,'testing new setup',NULL,'2025-01-12 16:38:43','2025-01-12 16:38:43',NULL,2),(14,'',NULL,'2025-01-12 16:52:06','2025-01-12 16:52:06',8,2),(15,'New Setup Working??',NULL,'2025-01-12 16:53:28','2025-01-12 16:53:28',9,1);
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
  `amount` decimal(10,2) DEFAULT '0.00',
  `collector_id` int DEFAULT NULL,
  `transaction_time` time DEFAULT NULL,
  `payment_plan_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `collector_id` (`collector_id`),
  KEY `fk_payment_plan_id` (`payment_plan_id`),
  CONSTRAINT `customer_transactions_ibfk_1` FOREIGN KEY (`collector_id`) REFERENCES `collectors` (`id`),
  CONSTRAINT `fk_payment_plan_id` FOREIGN KEY (`payment_plan_id`) REFERENCES `payment_plans` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_transactions`
--

LOCK TABLES `customer_transactions` WRITE;
/*!40000 ALTER TABLE `customer_transactions` DISABLE KEYS */;
INSERT INTO `customer_transactions` VALUES (1,'Emily Davis','2025-01-07',150.00,1,'21:17:55',NULL),(2,'Frank Moore','2025-01-07',200.00,2,'21:17:55',NULL),(3,'Grace Lee','2025-01-07',250.00,3,'21:17:55',NULL),(4,'Owen Davis ',NULL,200.00,NULL,NULL,NULL),(5,'Owen Davis ',NULL,200.00,NULL,NULL,NULL),(6,'Owen Davis ','2025-01-12',200.00,NULL,'15:20:00',NULL),(7,'Owen Davis ','2025-01-12',300.00,NULL,'16:17:00',NULL),(8,'Owen Davis','2025-01-12',500.00,NULL,'16:51:00',2),(9,'Owen Davis','2025-01-12',550.00,NULL,'16:53:00',3);
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

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `role` enum('admin','user') DEFAULT 'user',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'pretendemail@gmail.com','scrypt:32768:8:1$jdvpRzO7dLRkC2Uu$2f8982b3b8d1b6b2bdc93e4a0f971c6dfd646906aa23d2961910991f11111e7719dce8452e002838d5ffa5e23e68e6bb17b1f1372131a72076a15136019c2e19','user','2025-01-09 23:42:22'),(2,'admin@example.com','scrypt:32768:8:1$ChWFzpcTD6Og8RR9$7bae64908dc1eecc5e0ea2b00ed348188a86b15c6ee0b6770eb596e35eb9a7f10b9b05508cba7a32bb18c33370955943df9a7129882536a31efc9987a1539c1d','admin','2025-01-09 23:55:21');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-12 18:13:36
