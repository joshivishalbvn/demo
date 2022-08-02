-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 02, 2022 at 05:27 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rpi`
--

-- --------------------------------------------------------

--
-- Table structure for table `batch`
--

DROP TABLE IF EXISTS `batch`;
CREATE TABLE IF NOT EXISTS `batch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseid` int(11) NOT NULL,
  `batchtitle` varchar(20) NOT NULL,
  `start_date` varchar(11) NOT NULL,
  `end_date` varchar(11) NOT NULL,
  `class_time` varchar(20) NOT NULL,
  `isDeleted` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `batch`
--

INSERT INTO `batch` (`id`, `courseid`, `batchtitle`, `start_date`, `end_date`, `class_time`, `isDeleted`) VALUES
(7, 3, 'UPSC Batch', '01-01-2022', '01-10-2022', '07:00 To 11:00', 0),
(6, 1, '', '01-01-2022', '01-06-2022', '10:00 To 01:00', 0),
(5, 2, '', '01-08-2022', '01-02-2023', '09:00 To 12:00', 0),
(8, 3, '', '01-10-2022', '01-05-2023', '09:00 To 01:00', 0),
(9, 5, '', '05-08-2022', '01-02-2023', '07:00 To 10:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) NOT NULL,
  `fees` int(11) NOT NULL,
  `duration` varchar(10) NOT NULL,
  `description` varchar(128) NOT NULL,
  `isDeleted` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`id`, `title`, `fees`, `duration`, `description`, `isDeleted`) VALUES
(1, 'General Batch', 15000, '6', 'It Will Help In All Exam', 0),
(2, 'Talati Mantri', 15000, '6', 'Special Batch For Talati Mantri', 1),
(3, 'UPSC', 30000, '10', 'Best Batch For UPSC', 0),
(4, 'GPSC', 25000, '10', 'Best', 1),
(5, 'Constable', 10000, '6', 'For Constable Exam', 0);

-- --------------------------------------------------------

--
-- Table structure for table `lecture`
--

DROP TABLE IF EXISTS `lecture`;
CREATE TABLE IF NOT EXISTS `lecture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacherid` int(11) NOT NULL,
  `subjectid` int(11) NOT NULL,
  `batchid` int(11) NOT NULL,
  `duration` varchar(10) NOT NULL,
  `amount` int(11) NOT NULL,
  `lecturedate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `lecture`
--

INSERT INTO `lecture` (`id`, `teacherid`, `subjectid`, `batchid`, `duration`, `amount`, `lecturedate`) VALUES
(2, 1, 2, 2, '120', 4000, '2022-08-02 10:33:29'),
(3, 1, 2, 3, '120', 4000, '2022-08-02 10:33:29'),
(5, 1, 2, 2, '120', 4000, '2022-08-02 10:33:29'),
(6, 2, 1, 2, '60', 1500, '2022-08-02 10:33:29');

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
CREATE TABLE IF NOT EXISTS `subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseid` int(11) NOT NULL,
  `title` varchar(20) NOT NULL,
  `rate` int(11) NOT NULL,
  `isDeleted` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`id`, `courseid`, `title`, `rate`, `isDeleted`) VALUES
(1, 3, 'Maths', 3000, 0),
(2, 1, 'English', 4000, 0),
(3, 5, 'History', 3000, 0);

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
CREATE TABLE IF NOT EXISTS `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `mobile` int(12) NOT NULL,
  `email` varchar(128) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `experience` varchar(20) NOT NULL,
  `isDeleted` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`id`, `name`, `mobile`, `email`, `gender`, `qualification`, `experience`, `isDeleted`) VALUES
(1, 'Sandip Patel', 1234567891, 'sp@gmail.com', 'm', 'M.E', '10', 1),
(2, 'Raj Jambucha', 1234567890, 'raj@gmail.com', 'M', 'B.Ed', '10', 0),
(3, 'Vimal Ghoghari', 1234567895, 'vimal@gmail.com', 'M', 'B.Com', '5', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
