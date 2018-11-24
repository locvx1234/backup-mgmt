-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: backup_ctl
-- ------------------------------------------------------
-- Server version	5.7.24

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
-- Table structure for table `app_computer`
--

DROP TABLE IF EXISTS `app_computer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_computer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `name` varchar(45) NOT NULL,
  `platform` varchar(100) DEFAULT NULL,
  `ram` double DEFAULT NULL,
  `cpu` int(11) DEFAULT NULL,
  `allowed_capacity` double NOT NULL,
  `token` varchar(40) NOT NULL,
  `key` varchar(44) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_computer`
--

LOCK TABLES `app_computer` WRITE;
/*!40000 ALTER TABLE `app_computer` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_computer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_notification`
--

DROP TABLE IF EXISTS `app_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `issue` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_notification`
--

LOCK TABLES `app_notification` WRITE;
/*!40000 ALTER TABLE `app_notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_restorejob`
--

DROP TABLE IF EXISTS `app_restorejob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_restorejob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `path` varchar(1000) NOT NULL,
  `backup_id` int(11) NOT NULL,
  `time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  `computer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_restorejob_computer_id_79529acb_fk_app_computer_id` (`computer_id`),
  CONSTRAINT `app_restorejob_computer_id_79529acb_fk_app_computer_id` FOREIGN KEY (`computer_id`) REFERENCES `app_computer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_restorejob`
--

LOCK TABLES `app_restorejob` WRITE;
/*!40000 ALTER TABLE `app_restorejob` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_restorejob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_schedule`
--

DROP TABLE IF EXISTS `app_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime(6) NOT NULL,
  `typeofbackup` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `ip_server` varchar(21) NOT NULL,
  `path` varchar(1000) NOT NULL,
  `computer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_schedule_computer_id_ed974492_fk_app_computer_id` (`computer_id`),
  CONSTRAINT `app_schedule_computer_id_ed974492_fk_app_computer_id` FOREIGN KEY (`computer_id`) REFERENCES `app_computer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_schedule`
--

LOCK TABLES `app_schedule` WRITE;
/*!40000 ALTER TABLE `app_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_sync`
--

DROP TABLE IF EXISTS `app_sync`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_sync` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sync_time` datetime(6) NOT NULL,
  `amount_data_change` double NOT NULL,
  `path` varchar(1000) NOT NULL,
  `ip_server` varchar(21) NOT NULL,
  `status` varchar(100) NOT NULL,
  `computer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_sync_computer_id_890efe61_fk_app_computer_id` (`computer_id`),
  CONSTRAINT `app_sync_computer_id_890efe61_fk_app_computer_id` FOREIGN KEY (`computer_id`) REFERENCES `app_computer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_sync`
--

LOCK TABLES `app_sync` WRITE;
/*!40000 ALTER TABLE `app_sync` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_sync` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add computer',7,'add_computer'),(20,'Can change computer',7,'change_computer'),(21,'Can delete computer',7,'delete_computer'),(22,'Can add notification',8,'add_notification'),(23,'Can change notification',8,'change_notification'),(24,'Can delete notification',8,'delete_notification'),(25,'Can add restore job',9,'add_restorejob'),(26,'Can change restore job',9,'change_restorejob'),(27,'Can delete restore job',9,'delete_restorejob'),(28,'Can add schedule',10,'add_schedule'),(29,'Can change schedule',10,'change_schedule'),(30,'Can delete schedule',10,'delete_schedule'),(31,'Can add sync',11,'add_sync'),(32,'Can change sync',11,'change_sync'),(33,'Can delete sync',11,'delete_sync');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$NzSWX9leByXH$8zusQ2KmvoAHX4ZcYxBdl/gptIis1bk3gZMdTiY3tnk=','2018-11-24 04:04:16.195592',1,'admin','','','',1,1,'2018-08-24 04:04:02.920269');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-09-03 17:16:39.048750','9','/home/locvu/Downloads/example seveny',3,'',9,1),(2,'2018-09-03 17:16:39.055307','8','/home/locvu/Dropbox/loccode.py seveny',3,'',9,1),(3,'2018-09-03 17:16:39.057684','7','/home/locvu/Dropbox/loccode.py seveny',3,'',9,1),(4,'2018-09-03 17:16:39.061074','6','/home/locvu/Dropbox/loccode.py seveny',3,'',9,1),(5,'2018-09-03 17:16:39.063478','5','/home/locvu/Downloads/example seveny',3,'',9,1),(6,'2018-09-03 17:16:39.065095','4','/home/locvu/Dropbox/loccode.py seveny',3,'',9,1),(7,'2018-11-24 04:04:39.963170','1','seveny',3,'',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'app','computer'),(8,'app','notification'),(9,'app','restorejob'),(10,'app','schedule'),(11,'app','sync'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-08-24 04:03:35.062421'),(2,'auth','0001_initial','2018-08-24 04:03:35.778405'),(3,'admin','0001_initial','2018-08-24 04:03:35.939856'),(4,'admin','0002_logentry_remove_auto_add','2018-08-24 04:03:35.955643'),(5,'app','0001_initial','2018-08-24 04:03:36.273723'),(6,'contenttypes','0002_remove_content_type_name','2018-08-24 04:03:36.415625'),(7,'auth','0002_alter_permission_name_max_length','2018-08-24 04:03:36.426237'),(8,'auth','0003_alter_user_email_max_length','2018-08-24 04:03:36.444054'),(9,'auth','0004_alter_user_username_opts','2018-08-24 04:03:36.456094'),(10,'auth','0005_alter_user_last_login_null','2018-08-24 04:03:36.509877'),(11,'auth','0006_require_contenttypes_0002','2018-08-24 04:03:36.516365'),(12,'auth','0007_alter_validators_add_error_messages','2018-08-24 04:03:36.530505'),(13,'auth','0008_alter_user_username_max_length','2018-08-24 04:03:36.620368'),(14,'auth','0009_alter_user_last_name_max_length','2018-08-24 04:03:36.638282'),(15,'sessions','0001_initial','2018-08-24 04:03:36.686127'),(16,'app','0002_restorejob_status_text','2018-08-24 04:11:55.966209'),(17,'app','0003_auto_20180824_1118','2018-08-24 04:19:00.314001'),(18,'app','0004_auto_20180824_1120','2018-08-24 04:20:44.481284'),(19,'app','0005_auto_20180904_0017','2018-09-03 17:17:17.443713');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1gvmgddvband91p9f93fru72xoa64jey','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-09-11 16:53:48.920000'),('8q2dc04lle03f5ujpv6w6bp7gmh7tpw1','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-11-07 03:52:11.586078'),('9c530lyhij7pfgj93c2x84cj6n9u5n7i','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-10-19 16:45:33.787763'),('c3kur6rpu0bs1r1xv6ndz5e1j7f6yjv9','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-10-02 10:56:35.113035'),('cb734sl85n4546xvavc1bi9u9nl0as6r','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-12-08 04:04:16.206417'),('f3zfw8jrfcghxkdjyafs80elmgi3xmj6','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-09-07 04:04:32.464592'),('fc8ni4uykqhc1mgtrj8lnztbpliw8vrn','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-09-14 12:12:47.847159'),('gfs8kp274j3wd1nj9exdepsgetoo5qou','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-11-01 08:08:39.130044'),('hn2cl489uzhb3udl6rbux9ksczrdzx4e','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-09-10 16:57:39.772705'),('jv7fzt9vat6jd5fwb0wlii09mjkb31et','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-11-06 15:54:16.087787'),('k3pq2m48hsmpkydr1fj2m0yu3p6di4ez','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-09-17 09:29:05.199649'),('pmp7g1lb2ht9asqr8wodcncbz3dle1g5','YTJhZDg3NDAwNTVmMjE4M2Y3MmI4MmJhMjExMWNjMDgyY2JhYTgwNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlODFlMTMwNGNkMWMxZjFmMjYyOWNiNjI4OTMyMGJkNmQ2ZmNhNjA4In0=','2018-11-02 16:15:24.688641');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-24 11:13:43
