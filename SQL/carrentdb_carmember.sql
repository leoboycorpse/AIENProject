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
-- Table structure for table `carmember`
--

DROP TABLE IF EXISTS `carmember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carmember` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carmember`
--

LOCK TABLES `carmember` WRITE;
/*!40000 ALTER TABLE `carmember` DISABLE KEYS */;
INSERT INTO `carmember` VALUES (1,'Leo','1234','leo@gmail.com','2017-01-01','sam'),(2,'Leoboy','','leoboycorpse@gmail.com','0911','Taipei'),(3,'Leoboy','','leoboycorpse@gmail.com','0911','Taipei'),(4,'AAA','AAA','AAA@AAA.AAA','0955','AAA'),(5,'Ariel','ariel','Ariel@gmail.com','0911','興隆路QQ'),(6,'leo','0000','leo@hohtmail.com','0955201478','taipei'),(7,'Alex','0000','Alex@hotmial.com','0955815151','新北勢'),(8,'','leoo0720','leo@hotmail.com','0000',''),(9,'QQQ','QQQ','QQQ@QQQ.QQQ','0911111111','QQQ'),(10,'Test2','Test2','Try.@My.SQL','0933333333','Test2'),(11,'王大陸','setting','WuBigRoad@gmail.com','0981471235','新北市高雄區台中里行天宮'),(12,'大平台王大陸','3345678','BigflatTaiwan@gmail.com','0951478665','台北市天龍國環境保護局回收場21號B1'),(13,'WuBigRoad','WuBigRoad','WuBigRoad@hotmail.com','0952647885','新北市高雄區台中里行天宮'),(14,'朱笑天','test','Test@gmail.com','0911557849','高雄市仁愛路天龍街10號');
/*!40000 ALTER TABLE `carmember` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-26 11:01:13
