-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: carrentdb
-- ------------------------------------------------------
-- Server version	5.7.19-log

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
-- Table structure for table `carorder`
--

DROP TABLE IF EXISTS `carorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `days` int(11) NOT NULL,
  `area` varchar(45) NOT NULL,
  `returnarea` varchar(45) NOT NULL,
  `email` varchar(100) NOT NULL,
  `gettime` date NOT NULL,
  `booktime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carorder`
--

LOCK TABLES `carorder` WRITE;
/*!40000 ALTER TABLE `carorder` DISABLE KEYS */;
INSERT INTO `carorder` VALUES (1,'M4',4,'1','2','AAA@AAA.AAA','0000-00-00','2018-01-26 10:04:45'),(2,'cayenne',3,'2','3','Ariel@gmail.com','0000-00-00','2018-01-26 10:04:45'),(3,'i8',4,'3','1','leo@hohtmail.com','0000-00-00','2018-01-26 10:04:45'),(4,'M4',5,'1','2','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(5,'cayenne',2,'2','1','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(6,'M4',1,'1','2','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(7,'i8',1,'3','1','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(8,'M4',2,'1','1','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(9,'M4',2,'3','2','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(10,'cayenne',1,'1','3','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(11,'M4',1,'2','2','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(12,'M4',2,'三重區重新路一段','2','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(13,'BMW i8 (2017)',1,'大安區復興南路一段','三重區重新路一段','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(14,'BMW M4 (2018)',5,'三重區重新路一段','大安區復興南路一段','Try.@My.SQL','0000-00-00','2018-01-26 10:04:45'),(15,'BMW M4 (2018)',2,'大同區民權西路一段','大安區復興南路一段','QQQ@QQQ.QQQ','0000-00-00','2018-01-26 10:04:45'),(16,'BMW i8 (2017)',3,'大安區復興南路一段','大同區民權西路一段','WuBigRoad@hotmail.com','0000-00-00','2018-01-26 10:04:45'),(17,'BMW i8 (2017)',4,'三重區重新路一段','大安區復興南路一段','WuBigRoad@hotmail.com','0000-00-00','2018-01-26 10:04:45'),(18,'BMW i8 (2017)',2,'大同區民權西路一段','大安區復興南路一段','WuBigRoad@gmail.com','0000-00-00','2018-01-26 10:04:45'),(19,'BMW i8 (2017)',4,'三重區重新路一段','大安區復興南路一段','QQQ@QQQ.QQQ','2018-02-03','2018-01-26 10:04:45'),(20,'Porsche cayenne (2016)',7,'大安區復興南路一段','三重區重新路一段','BigflatTaiwan@gmail.com','2018-02-02','2018-01-26 10:06:33'),(21,'BMW i8 (2017)',5,'大安區復興南路一段','大同區民權西路一段','Test@gmail.com','2018-01-27','2018-01-26 10:55:16');
/*!40000 ALTER TABLE `carorder` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-26 11:01:15
