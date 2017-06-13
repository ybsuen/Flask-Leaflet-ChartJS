-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Jun 13, 2017 at 03:34 AM
-- Server version: 5.5.42
-- PHP Version: 5.6.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `datavizdemo`
--

-- --------------------------------------------------------

--
-- Table structure for table `destination`
--

CREATE TABLE `destination` (
  `id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `url` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `lat` float(10,6) NOT NULL,
  `lng` float(10,6) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `destination`
--

INSERT INTO `destination` (`id`, `name`, `url`, `lat`, `lng`) VALUES
(1, 'Victoria Peak', 'https://en.wikipedia.org/wiki/Victoria_Peak', 22.275900, 114.145500),
(2, 'Happy Valley', 'https://en.wikipedia.org/wiki/Happy_Valley,_Hong_Kong', 22.268400, 114.186501),
(3, 'Tsim Sha Tsui', 'https://en.wikipedia.org/wiki/Tsim_Sha_Tsui', 22.298800, 114.172203);

-- --------------------------------------------------------

--
-- Table structure for table `temperature`
--

CREATE TABLE `temperature` (
  `id` int(11) NOT NULL,
  `month` varchar(15) CHARACTER SET utf8 NOT NULL,
  `temperature` int(2) NOT NULL,
  `color` varchar(8) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `temperature`
--

INSERT INTO `temperature` (`id`, `month`, `temperature`, `color`) VALUES
(1, 'January', 16, '#95a5a6'),
(2, 'February', 18, '#34495e'),
(3, 'March', 20, '#2ecc71'),
(4, 'April', 24, '#e74c3c'),
(5, 'May', 26, '#f1c40f'),
(6, 'June', 28, '#34495e'),
(7, 'July', 29, '#9b59b6'),
(8, 'August', 29, '#34495e');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `destination`
--
ALTER TABLE `destination`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `temperature`
--
ALTER TABLE `temperature`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `destination`
--
ALTER TABLE `destination`
  MODIFY `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `temperature`
--
ALTER TABLE `temperature`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;