CREATE DATABASE  IF NOT EXISTS `svsinfo-2.0` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `svsinfo-2.0`;
-- MySQL dump 10.13  Distrib 5.5.16, for Win32 (x86)
--
-- Host: localhost    Database: svsinfo-2.0
-- ------------------------------------------------------
-- Server version	5.5.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `service_location`
--

LOCK TABLES `service_location` WRITE;
/*!40000 ALTER TABLE `service_location` DISABLE KEYS */;
INSERT INTO `service_location` VALUES (1,'Herning sportscenter');
/*!40000 ALTER TABLE `service_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `service_area`
--

LOCK TABLES `service_area` WRITE;
/*!40000 ALTER TABLE `service_area` DISABLE KEYS */;
INSERT INTO `service_area` VALUES (1,'Multihallen',1),(2,'Eventrum 1',1),(3,'Eventrum 2',1),(4,'Eventsalen',1),(5,'Cosplay hallen',1),(6,'Fan event området',1);
/*!40000 ALTER TABLE `service_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `service_activity`
--

LOCK TABLES `service_activity` WRITE;
/*!40000 ALTER TABLE `service_activity` DISABLE KEYS */;
INSERT INTO `service_activity` VALUES (1,'Velkomst','2012-05-11 19:00:00','2012-05-11 19:30:00',1,2),(2,'Auktion','2012-05-11 21:30:00','2012-05-12 01:30:00',1,1),(3,'Orienteringsløb','2012-05-11 21:30:00','2012-05-11 22:30:00',1,2),(4,'Musikquiz','2012-05-11 23:00:00','2012-05-11 23:40:00',1,2),(5,'Biografen åbner','2012-05-11 23:00:00','2012-05-12 03:00:00',1,3),(6,'Gæt et klip','2012-05-12 10:00:00','2012-05-12 11:00:00',1,1),(7,'In-character Hetalia panel','2012-05-12 10:00:00','2012-05-12 11:30:00',1,2),(8,'Holdquiz','2012-05-12 11:00:00','2012-05-12 13:00:00',1,1),(9,'Spilquiz','2012-05-12 13:00:00','2012-05-12 14:20:00',1,1),(10,'Chopstick Champion','2012-05-12 15:00:00','2012-05-12 16:30:00',1,1),(11,'Tegn og Gæt','2012-05-12 17:00:00','2012-05-12 18:30:00',1,1),(12,'Mafia','2012-05-13 00:00:00','2012-05-13 04:00:00',1,1),(13,'Hit med Anime’en!','2012-05-12 12:00:00','2012-05-12 13:00:00',1,2),(14,'Werewolves','2012-05-12 01:00:00','2012-05-12 03:00:00',1,1),(15,'Panel: Det danske fanmiljø','2012-05-12 13:00:00','2012-05-12 14:30:00',1,2),(16,'Turen går til japan','2012-05-12 14:30:00','2012-05-12 15:30:00',1,2),(17,'Surprise konsolkonkurrence','2012-05-12 16:00:00','2012-05-12 16:30:00',1,2),(18,'Speed-meeting','2012-05-12 09:30:00','2012-05-12 11:00:00',1,3),(19,'Yugioh turnering','2012-05-12 11:30:00','2012-05-12 16:30:00',1,3),(20,'DKos panel','2012-05-12 16:00:00','2012-05-12 17:30:00',1,3),(21,'Biografen åbner','2012-05-12 23:00:00','2012-05-13 03:00:00',1,3),(22,'Lolita loppemarked','2012-05-12 12:30:00','2012-05-12 14:30:00',1,4),(23,'Go fetch','2012-05-12 14:30:00','2012-05-12 15:30:00',1,4),(24,'Plushie rageri','2012-05-12 16:00:00','2012-05-12 17:00:00',1,4),(25,'Style pose off','2012-05-12 17:00:00','2012-05-12 18:30:00',1,4),(26,'Quizløb','2012-05-13 10:00:00','2012-05-13 12:00:00',1,1),(31,'EuroCosplay foredrag','2012-05-13 10:00:00','2012-05-13 10:50:00',1,2),(32,'Timeline Quiz','2012-05-13 11:00:00','2012-05-13 12:00:00',1,2),(35,'Kanji workshop','2012-05-13 10:00:00','2012-05-13 11:00:00',1,3),(36,'Tanto Cuore turnering','2012-05-13 11:00:00','2012-05-13 14:30:00',1,3);
/*!40000 ALTER TABLE `service_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `service_event`
--

LOCK TABLES `service_event` WRITE;
/*!40000 ALTER TABLE `service_event` DISABLE KEYS */;
INSERT INTO `service_event` VALUES (1,'SVScon 2012','2012-05-11 18:00:00','2012-05-13 15:00:00',1);
/*!40000 ALTER TABLE `service_event` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-10-20 20:39:33
