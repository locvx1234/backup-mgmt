-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: backup_sys
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
  `serial_number` varchar(50) NOT NULL,
  `name` varchar(45) NOT NULL,
  `os` varchar(45) NOT NULL,
  `ip_address` char(39) NOT NULL,
  `agent_version` bigint(20) NOT NULL,
  `ram` int(11) NOT NULL,
  `cpu` int(11) NOT NULL,
  `capacity_used` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_computer`
--

LOCK TABLES `app_computer` WRITE;
/*!40000 ALTER TABLE `app_computer` DISABLE KEYS */;
INSERT INTO `app_computer` VALUES (1,'DSDNJEHRW234324','Devstack','ubuntu','192.168.100.114',33751040,1023,1,30),(3,'qeqwdsd131','locvu-cent','CentOS','192.168.100.116',0,2015,1,100),(11,'4353rttre','Nagios','Ubuntu','192.167.2.23',16777216,2323,2,0),(21,'1235fdsfdvcdfg42','Openstack','Ubuntu','192.167.2.23',33816576,4096,4,0);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_notification`
--

LOCK TABLES `app_notification` WRITE;
/*!40000 ALTER TABLE `app_notification` DISABLE KEYS */;
INSERT INTO `app_notification` VALUES (1,'locvx1234@gmail.com',1);
/*!40000 ALTER TABLE `app_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_schedule`
--

DROP TABLE IF EXISTS `app_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime(6) NOT NULL,
  `computer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_schedule_computer_id_ed974492_fk_app_computer_id` (`computer_id`),
  CONSTRAINT `app_schedule_computer_id_ed974492_fk_app_computer_id` FOREIGN KEY (`computer_id`) REFERENCES `app_computer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_schedule`
--

LOCK TABLES `app_schedule` WRITE;
/*!40000 ALTER TABLE `app_schedule` DISABLE KEYS */;
INSERT INTO `app_schedule` VALUES (1,'2018-03-18 14:38:13.000000',NULL);
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
  `computer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_sync_computer_id_890efe61_fk_app_computer_id` (`computer_id`),
  CONSTRAINT `app_sync_computer_id_890efe61_fk_app_computer_id` FOREIGN KEY (`computer_id`) REFERENCES `app_computer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_sync`
--

LOCK TABLES `app_sync` WRITE;
/*!40000 ALTER TABLE `app_sync` DISABLE KEYS */;
INSERT INTO `app_sync` VALUES (2,'2018-03-18 14:36:00.000000',1.2,NULL),(3,'2018-03-17 14:37:14.000000',22.6,1),(4,'2018-03-17 05:00:00.000000',1.67,NULL),(5,'2018-03-17 23:00:00.000000',4.4,1),(6,'2018-03-18 15:04:59.000000',2.3,NULL),(7,'2018-03-18 15:36:04.000000',2.3,1),(8,'2018-03-19 15:52:40.000000',1,3),(9,'2018-03-18 16:05:16.000000',4,3);
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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add notification',7,'add_notification'),(20,'Can change notification',7,'change_notification'),(21,'Can delete notification',7,'delete_notification'),(22,'Can add computer',8,'add_computer'),(23,'Can change computer',8,'change_computer'),(24,'Can delete computer',8,'delete_computer'),(25,'Can add schedule',9,'add_schedule'),(26,'Can change schedule',9,'change_schedule'),(27,'Can delete schedule',9,'delete_schedule'),(28,'Can add sync',10,'add_sync'),(29,'Can change sync',10,'change_sync'),(30,'Can delete sync',10,'delete_sync');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$7KyOhvkGArZM$lcnpjuQHPHf9mFQ9WoAMofDWjPFCOMSm32KV6+FKtZc=','2018-03-18 14:10:19.537221',1,'locvu','','','',1,1,'2018-03-18 14:09:58.161064');
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-03-18 14:31:42.897894','1','Devstack 192.168.100.114',1,'[{\"added\": {}}]',8,1),(2,'2018-03-18 14:32:07.048398','2','cirros 192.16.161.1',1,'[{\"added\": {}}]',8,1),(3,'2018-03-18 14:36:05.613918','2','2018-03-18 21:36:00+07:00 cirros 192.16.161.1',1,'[{\"added\": {}}]',10,1),(4,'2018-03-18 14:37:21.318730','3','2018-03-17 21:37:14+07:00 Devstack 192.168.100.114',1,'[{\"added\": {}}]',10,1),(5,'2018-03-18 14:37:37.085672','4','2018-03-17 12:00:00+07:00 cirros 192.16.161.1',1,'[{\"added\": {}}]',10,1),(6,'2018-03-18 14:37:53.256601','5','2018-03-18 06:00:00+07:00 Devstack 192.168.100.114',1,'[{\"added\": {}}]',10,1),(7,'2018-03-18 14:38:20.706624','1','2018-03-18 21:38:13+07:00 cirros 192.16.161.1',1,'[{\"added\": {}}]',9,1),(8,'2018-03-18 14:39:58.902420','1','locvx1234@gmail.com [Warning]',1,'[{\"added\": {}}]',7,1),(9,'2018-03-18 14:45:46.143685','3','locvu-cent 192.168.100.116',1,'[{\"added\": {}}]',8,1),(10,'2018-03-18 15:05:02.328089','6','2018-03-18 22:04:59+07:00 cirros 192.16.161.1',1,'[{\"added\": {}}]',10,1),(11,'2018-03-18 15:36:12.711747','7','2018-03-18 22:36:04+07:00 Devstack 192.168.100.114',1,'[{\"added\": {}}]',10,1),(12,'2018-03-18 15:52:48.194684','8','2018-03-19 22:52:40+07:00 locvu-cent 192.168.100.116',1,'[{\"added\": {}}]',10,1),(13,'2018-03-18 16:05:20.522891','9','2018-03-18 23:05:16+07:00 locvu-cent 192.168.100.116',1,'[{\"added\": {}}]',10,1),(14,'2018-03-20 15:34:11.076033','1','Devstack 192.168.100.114',2,'[{\"changed\": {\"fields\": [\"agent_version\"]}}]',8,1),(15,'2018-03-21 13:52:31.593429','4','Openstack 192.167.2.23',2,'[{\"changed\": {\"fields\": [\"agent_version\", \"capacity_used\"]}}]',8,1),(16,'2018-03-21 13:52:55.019738','4','Openstack 192.167.2.23',3,'',8,1),(17,'2018-03-22 13:19:11.114010','6','Openstack 192.167.2.23',3,'',8,1),(18,'2018-03-22 13:19:15.732640','5','Openstack 192.167.2.23',3,'',8,1),(19,'2018-03-22 13:19:19.696470','9','osticket 8.8.8.7',3,'',8,1),(20,'2018-03-22 13:19:23.024741','7','osticket 8.8.8.7',3,'',8,1),(21,'2018-03-22 13:19:26.064494','8','osticket 8.8.8.7',3,'',8,1),(22,'2018-03-22 13:19:30.958109','10','osticket 8.8.8.7',3,'',8,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(8,'app','computer'),(7,'app','notification'),(9,'app','schedule'),(10,'app','sync'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-03-18 14:06:39.014772'),(2,'auth','0001_initial','2018-03-18 14:06:39.696493'),(3,'admin','0001_initial','2018-03-18 14:06:39.848253'),(4,'admin','0002_logentry_remove_auto_add','2018-03-18 14:06:39.857966'),(5,'app','0001_initial','2018-03-18 14:06:40.093426'),(6,'contenttypes','0002_remove_content_type_name','2018-03-18 14:06:40.176011'),(7,'auth','0002_alter_permission_name_max_length','2018-03-18 14:06:40.186714'),(8,'auth','0003_alter_user_email_max_length','2018-03-18 14:06:40.211001'),(9,'auth','0004_alter_user_username_opts','2018-03-18 14:06:40.225228'),(10,'auth','0005_alter_user_last_login_null','2018-03-18 14:06:40.307638'),(11,'auth','0006_require_contenttypes_0002','2018-03-18 14:06:40.314084'),(12,'auth','0007_alter_validators_add_error_messages','2018-03-18 14:06:40.328723'),(13,'auth','0008_alter_user_username_max_length','2018-03-18 14:06:40.416844'),(14,'auth','0009_alter_user_last_name_max_length','2018-03-18 14:06:40.443253'),(15,'sessions','0001_initial','2018-03-18 14:06:40.509730'),(16,'app','0002_auto_20180321_1952','2018-03-21 12:52:31.465352');
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
INSERT INTO `django_session` VALUES ('z0xro78j05ep93hnl5jgiwfljlqys5j3','NzhlNWJmY2JkZTBjNjM2ZjUzY2EwOGFiYWZlZmMyZThmOGRlOGM1Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjZhNjAzYjdlZTU2YzZhZmFiOWMzMWU3Mzc5ZTEwMzViOWUxMTc0YjEiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-04-01 14:10:19.547260');
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

-- Dump completed on 2018-03-23 15:20:17
