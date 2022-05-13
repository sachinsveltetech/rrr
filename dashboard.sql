-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: dashboard
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

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
-- Table structure for table `account_user`
--

DROP TABLE IF EXISTS `account_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `username` varchar(255) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `district_id` bigint DEFAULT NULL,
  `type` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `tsp_company_id` bigint DEFAULT NULL,
  `state_id` bigint DEFAULT NULL,
  `email` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `email` (`email`),
  KEY `account_user_tsp_company_id_feede7ae_fk_common_tsp_id` (`tsp_company_id`),
  KEY `account_user_district_id_b5d92114` (`district_id`),
  KEY `account_user_state_id_4b516da2_fk_common_state_id` (`state_id`),
  CONSTRAINT `account_user_district_id_b5d92114_fk_common_district_id` FOREIGN KEY (`district_id`) REFERENCES `common_district` (`id`),
  CONSTRAINT `account_user_state_id_4b516da2_fk_common_state_id` FOREIGN KEY (`state_id`) REFERENCES `common_state` (`id`),
  CONSTRAINT `account_user_tsp_company_id_feede7ae_fk_common_tsp_id` FOREIGN KEY (`tsp_company_id`) REFERENCES `common_tsp` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_user`
--

LOCK TABLES `account_user` WRITE;
/*!40000 ALTER TABLE `account_user` DISABLE KEYS */;
INSERT INTO `account_user` VALUES (4,'pbkdf2_sha256$320000$l5RIvussiOQI6eKS3ijw6k$ef9O9J1Nj17i8KS8uWwFC79GiVGDL13Sva66EmgRgWE=','2022-04-29 06:08:10.988841','sachin','8617809049',1,'SUPER_USER',1,1,NULL,NULL,NULL),(12,'pbkdf2_sha256$320000$MyvG84vHGJRtBqad6DuK1a$P2jea2sMPwNJQyoTAOdZiKBjYxTvz6F32smkbt9xBlI=',NULL,'user1','9876563845',1,'USER',1,0,NULL,2,'user1@gmail.com'),(13,'pbkdf2_sha256$320000$eS5AnfKdFDpz2n3cPi0bqM$hM/6PX59LkKm/2U1W1wvOq+iMIg/UNlVE2eHOG7+CV8=',NULL,'user2','9876563855',2,'USER',1,0,NULL,2,'user2@gmal.com'),(14,'pbkdf2_sha256$320000$Aoriyz9pKhYuA9z5KwdcvE$Ysrn9debuIhDnUAH2ADJh64htb6WPhKiboDkt/Aw37A=',NULL,'user3','9876563865',3,'USER',1,0,NULL,2,'user3@gmail.com'),(15,'pbkdf2_sha256$320000$3I55XbyFuv9ehLTMf2Bsoq$Y2d7lda+4uYFi6o584ventYnjT8tvLIFDg03rdwGizM=',NULL,'user4','9876563875',4,'USER',1,0,NULL,2,'user4@gmail.com'),(24,'pbkdf2_sha256$320000$YKZ0iJMOAqciPHmWgqgl32$aOX9oBAlDwGD6GpEGz8eS9+S3pzv/DkGkkRZtTWKhaQ=',NULL,'anand','9876563862',NULL,'ADMIN',1,0,NULL,2,'anand@gmail.com'),(25,'pbkdf2_sha256$320000$gnXmwYDP2zCKgA9UcZuzJC$fXFRldj66iXJH+fo52kq9FcaGkWxE3pPPVJESDzb8mU=',NULL,'nikhil','9876563872',2,'ADMIN',1,0,NULL,NULL,NULL),(26,'pbkdf2_sha256$320000$i6qkPxK9dj9lccL3Q4VwHY$3V2+bJtIvTsKC5Bo0pc5BxP4Jciey2hohW8d+1lhxVM=',NULL,'tspuserA','9876563871',NULL,'TSP',1,0,1,2,'tspuserA@gmail.com'),(27,'pbkdf2_sha256$320000$h2ot25Tj9jbNjcGfq8WzFg$90Wk19zbNUAA32Yi+GoXswa/qeHm4aNcGWFBBV8sdmI=',NULL,'tspuserJ','9876563873',NULL,'TSP',1,0,2,2,'tspuserJ@gmail.com'),(28,'pbkdf2_sha256$320000$6pkJADyz5IhKZGqB8NQAks$2c4GL1Gy3757Lj8u1cLtQx3sAwZ4WBjkD/UaNxA8cB0=',NULL,'tspuserB','9876563874',NULL,'TSP',1,0,3,2,'tspuserB@gmail.com'),(29,'pbkdf2_sha256$320000$jWNwgceUrUmiiJSU94s2S0$4l/j0rjVrpCYO6AMnLo5+b8h5xWYMB8kJssVwvuANYc=',NULL,'tspuserV','9876563876',NULL,'TSP',1,0,4,2,'tspuserV@gmail.com'),(30,'pbkdf2_sha256$320000$tXtpc6NLXKK8ucX2RC7xJJ$625h78tZBpbiYiuMhT1P5G43KdHZ9ohHRt2MKBc7pnE=',NULL,'abc','9876563879',NULL,'ADMIN',1,0,NULL,2,NULL),(31,'pbkdf2_sha256$320000$MC45oE64wyFFH9wcpRmR60$V9m9l+pv5p7wItXdHu8AkSLuzGRRJWJ9ftAqemPEh5Q=',NULL,'abcdefg','9876543456',NULL,'SUPER_USER',1,1,NULL,NULL,NULL),(32,'pbkdf2_sha256$320000$w1wOFndmdpwjdrUZiCKSBc$L0IZH/ZCRtFYnLl6T6xSw+qZkZw35zCCEwIVqtNJ9D8=',NULL,'abcde123','6978770743',NULL,'TSP',1,0,1,2,NULL),(33,'pbkdf2_sha256$320000$JclpzgeBBqeC5ycfin1841$guyPoX9TVEob6wnFSl+xqNfh5boh6gvHZNsXYBjfN3U=',NULL,'consequat','7775819913',NULL,'ADMIN',1,0,1,NULL,NULL),(34,'pbkdf2_sha256$320000$RUvecfJ6bDsTLtYzJvtNRE$tBTykqe594p3xauyhn4+Y9d16t5Azcfhh4FNQJAnlfw=',NULL,'consequataa','7775819911',NULL,'ADMIN',1,0,1,NULL,NULL),(35,'pbkdf2_sha256$320000$VH0pfUVmrhoUY0BOV4h1LA$UpVgPzxEMtVdUIX5wVPu6CMmVbnuW4ZNTCKI+Eccwm0=',NULL,'ab123','6978770744',5,'USER',1,0,NULL,2,'ab123@gmail.com'),(36,'pbkdf2_sha256$320000$O8gxEYySv8QerL7K1Xifje$rRMLgpeeN8iGBmgKUUudsf0ZdUMhPgoTkotiO1cOchQ=',NULL,'AAKK','7775819011',NULL,'USER',1,0,1,NULL,'gk@gmail.com');
/*!40000 ALTER TABLE `account_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add ip port',7,'add_ipport'),(26,'Can change ip port',7,'change_ipport'),(27,'Can delete ip port',7,'delete_ipport'),(28,'Can view ip port',7,'view_ipport'),(29,'Can add user request form',8,'add_userrequestform'),(30,'Can change user request form',8,'change_userrequestform'),(31,'Can delete user request form',8,'delete_userrequestform'),(32,'Can view user request form',8,'view_userrequestform'),(33,'Can add tsp',9,'add_tsp'),(34,'Can change tsp',9,'change_tsp'),(35,'Can delete tsp',9,'delete_tsp'),(36,'Can view tsp',9,'view_tsp'),(37,'Can add state',10,'add_state'),(38,'Can change state',10,'change_state'),(39,'Can delete state',10,'delete_state'),(40,'Can view state',10,'view_state'),(41,'Can add district',11,'add_district'),(42,'Can change district',11,'change_district'),(43,'Can delete district',11,'delete_district'),(44,'Can view district',11,'view_district'),(45,'Can add rejection table',12,'add_rejectiontable'),(46,'Can change rejection table',12,'change_rejectiontable'),(47,'Can delete rejection table',12,'delete_rejectiontable'),(48,'Can view rejection table',12,'view_rejectiontable');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `common_district`
--

DROP TABLE IF EXISTS `common_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `common_district` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `state_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `common_district_state_id_b0c3eb84_fk_common_state_id` (`state_id`),
  CONSTRAINT `common_district_state_id_b0c3eb84_fk_common_state_id` FOREIGN KEY (`state_id`) REFERENCES `common_state` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `common_district`
--

LOCK TABLES `common_district` WRITE;
/*!40000 ALTER TABLE `common_district` DISABLE KEYS */;
INSERT INTO `common_district` VALUES (1,'Baksa',2),(2,'Barpeta',2),(3,'Biswanath',2),(4,'Bongaigaon',2),(5,'Cachar',2),(6,'Charaideo',2),(7,'Chirang',2),(8,'Darrang',2),(9,'Dhemaji',2),(10,'Dhubri',2),(11,'Dibrugarh',2),(12,'Dima Hasao (North Cachar Hills)',2),(13,'Goalpara',2),(14,'Golaghat',2),(15,'Hailakandi',2),(16,'Hojai',2),(17,'Jorhat',2),(18,'Kamrup',2),(19,'Kamrup Metropolitan',2),(20,'Karbi Anglong',2),(21,'Karimganj',2),(22,'Kokrajhar',2),(23,'Lakhimpur',2),(24,'Majuli',2),(25,'Morigaon',2),(26,'Nagaon',2),(27,'Nalbari',2),(28,'S-Z',2),(29,'Sivasagar',2),(30,'Sonitpur',2),(31,'South Salamara-Mankachar',2),(32,'Tinsukia',2),(33,'Udalguri',2),(34,'West Karbi Anglong',2);
/*!40000 ALTER TABLE `common_district` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `common_state`
--

DROP TABLE IF EXISTS `common_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `common_state` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `common_state`
--

LOCK TABLES `common_state` WRITE;
/*!40000 ALTER TABLE `common_state` DISABLE KEYS */;
INSERT INTO `common_state` VALUES (1,'ANDHRA PRADESH'),(2,'ASSAM'),(3,'ARUNACHAL PRADESH'),(4,'BIHAR'),(5,'GUJRAT'),(6,'HARYANA'),(7,'HIMACHAL PRADESH'),(8,'JAMMU & KASHMIR'),(9,'KARNATAKA'),(10,'KERALA'),(11,'MADHYA PRADESH'),(12,'MAHARASHTRA'),(13,'MANIPUR'),(14,'MEGHALAYA'),(15,'MIZORAM'),(16,'NAGALAND'),(17,'ORISSA'),(18,'PUNJAB'),(19,'RAJASTHAN'),(20,'SIKKIM'),(21,'TAMIL NADU'),(22,'TRIPURA'),(23,'UTTAR PRADESH'),(24,'WEST BENGAL'),(25,'DELHI'),(26,'GOA'),(27,'PONDICHERY'),(28,'LAKSHDWEEP'),(29,'DAMAN & DIU'),(30,'DADRA & NAGAR'),(31,'CHANDIGARH'),(32,'ANDAMAN & NICOBAR'),(33,'UTTARANCHAL'),(34,'JHARKHAND'),(35,'CHATTISGARH');
/*!40000 ALTER TABLE `common_state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `common_tsp`
--

DROP TABLE IF EXISTS `common_tsp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `common_tsp` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `common_tsp`
--

LOCK TABLES `common_tsp` WRITE;
/*!40000 ALTER TABLE `common_tsp` DISABLE KEYS */;
INSERT INTO `common_tsp` VALUES (1,'AIRTEL'),(2,'JIO'),(3,'BSNL'),(4,'VI');
/*!40000 ALTER TABLE `common_tsp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_account_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_account_user_id` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (5,'2022-04-29 07:17:03.103007','8','ananduseoooor',3,'',6,4),(6,'2022-04-29 10:37:18.669717','9','ananduseoooor',3,'',6,4),(7,'2022-04-29 10:40:08.495557','10','user1',3,'',6,4),(8,'2022-04-29 10:40:08.510746','11','user2',3,'',6,4);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'account','user'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(11,'common','district'),(10,'common','state'),(9,'common','tsp'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(7,'user_request_form','ipport'),(12,'user_request_form','rejectiontable'),(8,'user_request_form','userrequestform');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'common','0001_initial','2022-04-28 12:11:54.359413'),(2,'account','0001_initial','2022-04-28 12:11:54.463878'),(3,'contenttypes','0001_initial','2022-04-28 12:11:54.508949'),(4,'admin','0001_initial','2022-04-28 12:11:54.651361'),(5,'admin','0002_logentry_remove_auto_add','2022-04-28 12:11:54.657384'),(6,'admin','0003_logentry_add_action_flag_choices','2022-04-28 12:11:54.663225'),(7,'contenttypes','0002_remove_content_type_name','2022-04-28 12:11:54.755973'),(8,'auth','0001_initial','2022-04-28 12:11:55.041525'),(9,'auth','0002_alter_permission_name_max_length','2022-04-28 12:11:55.111414'),(10,'auth','0003_alter_user_email_max_length','2022-04-28 12:11:55.119391'),(11,'auth','0004_alter_user_username_opts','2022-04-28 12:11:55.127059'),(12,'auth','0005_alter_user_last_login_null','2022-04-28 12:11:55.144924'),(13,'auth','0006_require_contenttypes_0002','2022-04-28 12:11:55.149992'),(14,'auth','0007_alter_validators_add_error_messages','2022-04-28 12:11:55.163603'),(15,'auth','0008_alter_user_username_max_length','2022-04-28 12:11:55.171756'),(16,'auth','0009_alter_user_last_name_max_length','2022-04-28 12:11:55.181852'),(17,'auth','0010_alter_group_name_max_length','2022-04-28 12:11:55.206481'),(18,'auth','0011_update_proxy_permissions','2022-04-28 12:11:55.215150'),(19,'auth','0012_alter_user_first_name_max_length','2022-04-28 12:11:55.221795'),(20,'common','0002_state_district','2022-04-28 12:11:55.351573'),(21,'sessions','0001_initial','2022-04-28 12:11:55.396189'),(22,'user_request_form','0001_initial','2022-04-28 12:11:55.733185'),(23,'common','0003_alter_district_options_alter_state_options','2022-04-29 05:07:07.723283'),(24,'account','0002_alter_user_district','2022-04-29 05:07:07.926622'),(25,'common','0004_alter_tsp_options','2022-05-04 07:21:06.170064'),(26,'user_request_form','0002_userrequestform_decision_taken_by_rejectiontable','2022-05-04 07:21:06.397021'),(27,'user_request_form','0003_remove_rejectiontable_rejected_by_and_more','2022-05-04 07:31:35.143478'),(28,'user_request_form','0004_remove_userrequestform_reject_msg_and_more','2022-05-04 09:14:34.848651'),(29,'user_request_form','0002_alter_userrequestform_observer_account_type','2022-05-05 07:16:26.656111'),(30,'user_request_form','0002_rejectiontable_reject_by','2022-05-05 07:29:04.724593'),(31,'account','0002_user_state','2022-05-06 07:20:57.316484'),(32,'account','0003_alter_user_district','2022-05-06 08:43:03.555389'),(33,'user_request_form','0003_userrequestform_admin_status_and_more','2022-05-09 06:05:20.754035'),(34,'user_request_form','0004_alter_userrequestform_admin_status_and_more','2022-05-09 09:11:40.439904'),(35,'user_request_form','0005_alter_userrequestform_replied_date','2022-05-09 09:12:44.648815'),(36,'user_request_form','0006_remove_userrequestform_tsp_status','2022-05-09 10:45:27.710124'),(37,'user_request_form','0007_remove_userrequestform_date_from_and_more','2022-05-11 05:20:27.872419'),(38,'account','0004_user_email','2022-05-13 05:28:04.921786');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('bywe03oa5lxoogku8y8o21vaovw5ttgd','.eJxVjDsOwjAQBe_iGlnG8S-U9DmDtd714gCypTipEHeHSCmgfTPzXiLCtpa49bzEmcRFGHH63RLgI9cd0B3qrUlsdV3mJHdFHrTLqVF-Xg_376BAL99aD-DTWQ_JAmo3ZB49JGvZUlbG-WA4-JyARzKGSWnLhISs0LD3gZx4fwD3NTjU:1nkJnW:BkagA3x0_yQwvayijg2nqYU-jgflOt53csV-NpyM2fk','2022-05-13 06:08:10.993693');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_request_form_ipport`
--

DROP TABLE IF EXISTS `user_request_form_ipport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_request_form_ipport` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ip` varchar(200) NOT NULL,
  `port` int NOT NULL,
  `date_from` date DEFAULT NULL,
  `date_to` date DEFAULT NULL,
  `time_from` time(6) DEFAULT NULL,
  `time_to` time(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_request_form_ipport`
--

LOCK TABLES `user_request_form_ipport` WRITE;
/*!40000 ALTER TABLE `user_request_form_ipport` DISABLE KEYS */;
INSERT INTO `user_request_form_ipport` VALUES (1,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(2,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(3,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(4,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(5,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(6,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(7,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(8,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(9,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(10,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(11,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(12,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(13,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(14,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(15,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(16,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(17,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(18,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(19,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(20,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(21,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(22,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(23,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(24,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(25,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(26,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(27,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(28,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(29,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(30,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(31,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(32,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(33,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(34,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(35,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(36,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(37,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(38,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(39,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(40,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(41,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(42,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(43,'22.22.123.22',2234,NULL,NULL,NULL,NULL),(44,'33.33.123.33',2235,NULL,NULL,NULL,NULL),(45,'44.44.123.44',2255,NULL,NULL,NULL,NULL),(46,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(47,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(48,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(49,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(50,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(51,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(52,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(53,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(54,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(55,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(56,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(57,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(58,'22.22.123.22',3333,NULL,NULL,NULL,NULL),(59,'24.23.123.23',3335,NULL,NULL,NULL,NULL),(60,'11.11.123.11',1010,NULL,NULL,NULL,NULL),(61,'12.12.123.12',1111,NULL,NULL,NULL,NULL),(62,'13.13.123.13',1212,NULL,NULL,NULL,NULL),(63,'11.11.123.11',1010,'2022-04-12','2022-04-12','06:05:02.000000','06:05:03.000000'),(64,'12.12.123.12',1111,'2022-04-12','2022-04-12','06:05:02.000000','06:05:03.000000'),(65,'13.13.123.13',1212,'2022-04-12','2022-04-12','06:05:02.000000','06:05:03.000000'),(66,'11.11.123.11',3030,NULL,NULL,NULL,NULL),(67,'11.11.123.11',3030,'2022-02-02','2022-09-09','06:00:00.000000','06:00:00.000000'),(68,'11.11.123.12',3032,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(69,'11.11.123.13',3034,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(70,'11.11.123.13',3034,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(71,'11.11.123.13',3034,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(72,'11.11.123.13',3034,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(73,'11.11.123.13',3034,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(74,'11.11.123.13',3034,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(75,'11.11.123.13',3034,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(76,'11.11.123.13',3034,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(77,'11.11.123.13',3034,'2022-05-12','2022-05-19','06:00:00.000000','06:00:00.000000'),(78,'11.11.123.11',33333,NULL,NULL,NULL,NULL),(79,'11.11.123.11',33333,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user_request_form_ipport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_request_form_rejectiontable`
--

DROP TABLE IF EXISTS `user_request_form_rejectiontable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_request_form_rejectiontable` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rejection_time` datetime(6) NOT NULL,
  `rejection_reason` varchar(500) DEFAULT NULL,
  `user_form_id` bigint NOT NULL,
  `reject_by_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_request_form_re_user_form_id_6e17539f_fk_user_requ` (`user_form_id`),
  KEY `user_request_form_re_reject_by_id_f922c971_fk_account_u` (`reject_by_id`),
  CONSTRAINT `user_request_form_re_reject_by_id_f922c971_fk_account_u` FOREIGN KEY (`reject_by_id`) REFERENCES `account_user` (`id`),
  CONSTRAINT `user_request_form_re_user_form_id_6e17539f_fk_user_requ` FOREIGN KEY (`user_form_id`) REFERENCES `user_request_form_userrequestform` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_request_form_rejectiontable`
--

LOCK TABLES `user_request_form_rejectiontable` WRITE;
/*!40000 ALTER TABLE `user_request_form_rejectiontable` DISABLE KEYS */;
INSERT INTO `user_request_form_rejectiontable` VALUES (1,'2022-05-04 07:31:43.998643','jsdcknc kchkck skskakn',1,NULL),(3,'2022-05-05 09:05:27.182201','jsdcknc kchkck skskasdfsdkjckn',2,NULL),(4,'2022-05-05 09:07:42.133597','jsdcknc kchkck skskasdfsdkjckn',2,24),(5,'2022-05-05 09:08:06.239115','jsdcknc kchkck skskasdfsdkjckn',3,25),(6,'2022-05-05 09:08:15.872981','jsdcknc kchkck skskasdfsdkjckn',3,24),(7,'2022-05-05 09:08:20.859535','jsdcknc kchkck skskasdfsdkjckn',3,25),(8,'2022-05-06 14:17:26.294133','incomplete info',19,24),(9,'2022-05-13 07:30:56.136609','cupidatat labore fugiat nisi',15,NULL),(10,'2022-05-13 08:23:21.960954','absjasjc ajdbajdjan asdbasbd',6,24),(11,'2022-05-13 08:27:57.705534','absjasjc ajdbajdjan asdbasbd',19,24),(12,'2022-05-13 09:05:29.095201','This is rejection test',36,24);
/*!40000 ALTER TABLE `user_request_form_rejectiontable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_request_form_userrequestform`
--

DROP TABLE IF EXISTS `user_request_form_userrequestform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_request_form_userrequestform` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `sys_date` date NOT NULL,
  `sys_time` time(6) NOT NULL,
  `target_type` varchar(200) NOT NULL,
  `case_ref` varchar(200) NOT NULL,
  `case_type` varchar(200) NOT NULL,
  `request_to_provide` varchar(200) NOT NULL,
  `mobile_number` bigint NOT NULL,
  `cell_id` varchar(200) NOT NULL,
  `imei` varchar(200) NOT NULL,
  `duration_date_from` date NOT NULL,
  `duration_date_to` date NOT NULL,
  `duration_time_from` time(6) NOT NULL,
  `duration_time_to` time(6) NOT NULL,
  `user_file` varchar(100) NOT NULL,
  `form_status` varchar(200) DEFAULT NULL,
  `requested_date` date DEFAULT NULL,
  `replied_date` date DEFAULT NULL,
  `approval_or_reject_date` date DEFAULT NULL,
  `approval_or_reject_time` time(6) DEFAULT NULL,
  `tsp_file` varchar(100) NOT NULL,
  `select_tsp_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `decision_taken_by_id` bigint DEFAULT NULL,
  `observer_account_type` varchar(200) NOT NULL,
  `admin_status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_request_form_us_select_tsp_id_f2f000ba_fk_common_ts` (`select_tsp_id`),
  KEY `user_request_form_us_user_id_484065cb_fk_account_u` (`user_id`),
  KEY `user_request_form_us_decision_taken_by_id_e14293f5_fk_account_u` (`decision_taken_by_id`),
  CONSTRAINT `user_request_form_us_decision_taken_by_id_e14293f5_fk_account_u` FOREIGN KEY (`decision_taken_by_id`) REFERENCES `account_user` (`id`),
  CONSTRAINT `user_request_form_us_select_tsp_id_f2f000ba_fk_common_ts` FOREIGN KEY (`select_tsp_id`) REFERENCES `common_tsp` (`id`),
  CONSTRAINT `user_request_form_us_user_id_484065cb_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_request_form_userrequestform`
--

LOCK TABLES `user_request_form_userrequestform` WRITE;
/*!40000 ALTER TABLE `user_request_form_userrequestform` DISABLE KEYS */;
INSERT INTO `user_request_form_userrequestform` VALUES (1,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','IPDR',9876543221,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','REJECT','2022-04-12','2022-04-12','2022-05-06','04:53:00.000000','',3,24,24,'ADMIN','APPROVE'),(2,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','TDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','user_doc/sachin.odt','APPROVE','2022-04-12','2022-04-12',NULL,NULL,'',3,24,NULL,'USER','APPROVE'),(3,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','IPDR',9876543223,'112222333','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','REJECT','2022-04-12','2022-04-12',NULL,NULL,'',3,12,24,'ADMIN','REJECT'),(4,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','CDR',9876543224,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','REJECT','2022-04-12','2022-04-12',NULL,NULL,'',3,12,NULL,'USER','PENDING'),(5,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','SDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',3,12,NULL,'USER','PENDING'),(6,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','IPDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','REJECT','2022-04-12','2022-04-12','2022-05-06','05:47:00.000000','',1,12,24,'ADMIN','REJECT'),(7,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','TDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',1,12,NULL,'USER','APPROVE'),(8,'2021-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','SDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',1,12,NULL,'USER','PENDING'),(9,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','CDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',1,12,NULL,'USER','PENDING'),(10,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','IPDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',2,12,24,'ADMIN','APPROVE'),(11,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','TDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',2,12,24,'ADMIN','APPROVE'),(12,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','CDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',2,12,NULL,'USER','PENDING'),(13,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','SDR',9876543222,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',2,12,NULL,'USER','PENDING'),(14,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','SDR',9876543123,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',1,13,NULL,'USER','PENDING'),(15,'2022-04-22','10:00:00.000000','IMEI_NUMBER','12323','ABC','IPDR',9832876542,'12331','1234567890987654','2022-04-19','2022-05-19','10:00:00.000000','06:00:00.000000','','PENDING','2022-04-19','2022-04-22',NULL,NULL,'',4,14,24,'ADMIN','APPROVE'),(16,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','TDR',9876543134,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',1,14,24,'ADMIN','APPROVE'),(17,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','SDR',9876542134,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',1,14,NULL,'USER','PENDING'),(18,'2022-04-15','06:05:18.000000','IMEI_NUMBER','01/1234/123456D','DEC','CDR',9876522134,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',2,14,NULL,'USER','PENDING'),(19,'2022-04-22','10:00:00.000000','IMEI_NUMBER','12323','ABC','IPDR',9832876542,'2','1234567890987654','2022-04-19','2022-05-19','10:00:00.000000','06:00:00.000000','','PENDING','2022-04-19','2022-04-22',NULL,NULL,'',4,12,24,'ADMIN','REJECT'),(20,'2022-05-10','02:30:00.000000','CELL_ID','123asd','CDC','IPDR',9876543210,'12314','1231253454364565','2022-05-10','2022-05-19','10:00:00.000000','06:00:00.000000','user_doc/sachin2_UUO5OuW.odt','PENDING',NULL,NULL,NULL,NULL,'',1,12,24,'USER','APPROVE'),(21,'2022-04-15','06:05:18.000000','IP_ADDRESS','01/1234/123456D','DEC','IPDR',9876543223,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','PENDING','2022-04-12','2022-04-12',NULL,NULL,'',3,12,24,'ADMIN','APPROVE'),(22,'2022-04-15','06:05:18.000000','IP_ADDRESS','01/1234/123456D','DEC','IPDR',9876543223,'1223555','12234567899877654','2022-04-12','2022-04-12','06:05:08.000000','06:05:09.000000','','REJECT','2022-04-12','2022-04-12',NULL,NULL,'',3,12,24,'ADMIN','REJECT'),(23,'2022-02-02','09:00:00.000000','CELL_ID','1233','CDC','IPDR',9876543421,'1231231','12321423535465775675','2022-09-09','2022-10-10','09:00:00.000000','10:00:00.000000','user_doc/sachin_sKLV7IU.odt','PENDING',NULL,NULL,NULL,NULL,'',3,12,NULL,'USER','PENDING'),(24,'2022-02-02','09:00:00.000000','CELL_ID','1233','CDC','IPDR',9876543421,'1231231','12321423535465775675','2022-09-09','2022-10-10','09:00:00.000000','10:00:00.000000','user_doc/sachin_dm0etxt.odt','PENDING',NULL,NULL,NULL,NULL,'',3,12,NULL,'USER','PENDING'),(25,'2022-05-11','10:00:00.000000','IMEI_NUMBER','05/9876/123456R','CDC','IPDR',9876543420,'1231231','12321423535465775675','2022-05-12','2022-05-12','10:00:00.000000','10:00:00.000000','user_doc/sachin_kwjJcbM.odt','PENDING',NULL,NULL,NULL,NULL,'',1,13,NULL,'USER','PENDING'),(26,'2022-05-12','10:00:00.000000','MOBILE_NUMBER','05/9876/123456T','CDC','TDR',9876543410,'1231','12321423535465775673','2022-05-12','2022-05-19','10:00:00.000000','10:00:00.000000','user_doc/sachin_xxOwJSh.odt','PENDING',NULL,NULL,NULL,NULL,'',2,13,NULL,'USER','PENDING'),(27,'2022-05-12','10:00:00.000000','IP_ADDRESS','05/9876/123456G','CDC','SDR',9876543420,'12312','12321423535465775672','2022-05-12','2022-05-19','10:00:00.000000','10:00:00.000000','user_doc/sachin_6lOSEew.odt','PENDING',NULL,NULL,NULL,NULL,'',3,13,NULL,'USER','PENDING'),(28,'2022-05-05','10:00:00.000000','IP_ADDRESS','05/9876/123456G','CDC','CDR',9876543420,'12312','12321423535465775672','2022-05-12','2022-05-19','10:00:00.000000','10:00:00.000000','user_doc/sachin_Q5byrFa.odt','PENDING',NULL,NULL,NULL,NULL,'',4,13,NULL,'USER','PENDING'),(29,'2022-05-05','10:00:00.000000','MOBILE_NUMBER','05/9876/123456R','CDC','IPDR',9876543421,'12312','12321423535465775672','2022-05-12','2022-05-19','10:00:00.000000','10:00:00.000000','user_doc/sachin_g7L1DN5.odt','PENDING',NULL,NULL,NULL,NULL,'',1,15,NULL,'USER','PENDING'),(30,'2022-05-05','10:00:00.000000','IMEI_NUMBER','05/9876/123456E','CDF','TDR',9876543422,'12312','12321423535465775676','2022-05-12','2022-05-19','10:00:00.000000','10:00:00.000000','user_doc/sachin_sUmDL9h.odt','PENDING',NULL,NULL,NULL,NULL,'',2,15,NULL,'USER','PENDING'),(31,'2022-05-05','10:00:00.000000','CELL_ID','05/9876/123456W','CDF','SDR',9876543422,'12312','12321423535465775676','2022-05-12','2022-05-19','10:00:00.000000','10:00:00.000000','user_doc/sachin_LMUWeSt.odt','PENDING',NULL,NULL,NULL,NULL,'',3,15,NULL,'USER','PENDING'),(32,'2022-05-05','10:00:00.000000','IP_ADDRESS','05/9876/123456W','CDF','CDR',9876543422,'12312','12321423535465775676','2022-05-12','2022-05-19','10:00:00.000000','10:00:00.000000','user_doc/sachin_h8o10dX.odt','PENDING',NULL,NULL,NULL,NULL,'',4,15,NULL,'USER','PENDING'),(33,'2022-05-05','10:00:00.000000','IP_ADDRESS','05/9876/123456W','CDF','CDR',9876543422,'12312','12321423535465775676','2022-05-12','2022-05-19','10:00:00.000000','10:00:00.000000','user_doc/sachin_e68R9gW.odt','PENDING',NULL,NULL,NULL,NULL,'',4,15,NULL,'USER','PENDING'),(34,'2022-05-05','10:00:00.000000','IP_ADDRESS','05/9876/123456W','CDF','CDR',9876543422,'12312','12321423535465775676','2022-05-12','2022-05-19','10:00:00.000000','10:00:00.000000','user_doc/sachin_cydOR4x.odt','PENDING',NULL,NULL,NULL,NULL,'',4,15,NULL,'USER','PENDING'),(35,'2022-02-02','09:00:00.000000','CELL_ID','1233','CDC','IPDR',9876543421,'1231231','12321423535465775675','2022-09-09','2022-10-10','09:00:00.000000','10:00:00.000000','','PENDING',NULL,NULL,NULL,NULL,'',3,12,NULL,'USER','PENDING'),(36,'2022-02-02','09:00:00.000000','CELL_ID','1233','CDC','IPDR',9876543421,'1231231','12321423535465775675','2022-09-09','2022-10-10','09:00:00.000000','10:00:00.000000','','REJECT',NULL,NULL,NULL,NULL,'',3,12,24,'ADMIN','REJECT');
/*!40000 ALTER TABLE `user_request_form_userrequestform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_request_form_userrequestform_ip_port`
--

DROP TABLE IF EXISTS `user_request_form_userrequestform_ip_port`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_request_form_userrequestform_ip_port` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userrequestform_id` bigint NOT NULL,
  `ipport_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_request_form_userre_userrequestform_id_ippor_c32cf11a_uniq` (`userrequestform_id`,`ipport_id`),
  KEY `user_request_form_us_ipport_id_6ca9fe58_fk_user_requ` (`ipport_id`),
  CONSTRAINT `user_request_form_us_ipport_id_6ca9fe58_fk_user_requ` FOREIGN KEY (`ipport_id`) REFERENCES `user_request_form_ipport` (`id`),
  CONSTRAINT `user_request_form_us_userrequestform_id_50129cb8_fk_user_requ` FOREIGN KEY (`userrequestform_id`) REFERENCES `user_request_form_userrequestform` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_request_form_userrequestform_ip_port`
--

LOCK TABLES `user_request_form_userrequestform_ip_port` WRITE;
/*!40000 ALTER TABLE `user_request_form_userrequestform_ip_port` DISABLE KEYS */;
INSERT INTO `user_request_form_userrequestform_ip_port` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,4),(5,2,5),(6,2,6),(9,3,7),(7,3,8),(8,3,9),(10,4,10),(11,4,11),(12,4,12),(13,5,13),(14,5,14),(15,5,15),(16,6,16),(17,6,17),(18,6,18),(19,7,19),(20,7,20),(21,7,21),(23,8,22),(24,8,23),(22,8,24),(25,9,25),(26,9,26),(27,9,27),(28,10,28),(29,10,29),(30,10,30),(33,11,31),(31,11,32),(32,11,33),(34,12,34),(35,12,35),(36,12,36),(37,13,37),(38,13,38),(39,13,39),(40,14,40),(41,14,41),(42,14,42),(43,15,43),(44,15,44),(45,15,45),(47,16,46),(48,16,47),(46,16,48),(49,17,49),(50,17,50),(51,17,51),(52,18,52),(53,18,53),(54,18,54),(57,19,55),(55,19,56),(56,19,57),(58,20,58),(59,20,59),(60,21,60),(61,21,61),(62,21,62),(65,22,63),(63,22,64),(64,22,65),(66,23,66),(67,24,67),(68,25,68),(69,26,69),(70,27,70),(71,28,71),(72,29,72),(73,30,73),(74,31,74),(75,32,75),(76,33,76),(77,34,77),(78,35,78),(79,36,79);
/*!40000 ALTER TABLE `user_request_form_userrequestform_ip_port` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-13 14:56:18
