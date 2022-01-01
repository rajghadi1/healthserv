-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: remotemysql.com
-- Generation Time: Dec 31, 2021 at 04:42 AM
-- Server version: 8.0.13-4
-- PHP Version: 7.2.24-0ubuntu0.18.04.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `0dUfVC8t7r`
--
CREATE DATABASE IF NOT EXISTS `0dUfVC8t7r` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `0dUfVC8t7r`;

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `user_id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `subject` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `message` longtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`user_id`, `name`, `email`, `subject`, `message`) VALUES
(1, 'testerq', 'tester@besterqq', 'ghskjbh', 'hjkds'),
(2, 'jnj', 'nkn@gyu', 'jknkjnkjn', 'kjn'),
(3, 'jnj', 'nkn@gyu', 'jknkjnkjn', 'kjn'),
(4, 'jnj', 'nkn@gyu', 'jknkjnkjn', 'kjn'),
(5, 'jnj', 'nkn@gyu', 'jknkjnkjn', 'kjn'),
(6, 'jnj', 'nkn@gyu', 'jknkjnkjn', 'kjn'),
(7, 'jnj', 'nkn@gyu', 'jknkjnkjn', 'kjn'),
(8, 'jnj', 'nkn@gyu', 'jknkjnkjn', 'kjn'),
(9, 'testerq', 'tester@besterqq', 'kjefnjkn', 'kjdnk'),
(10, 'fdsjhb', 'vjnfk@dskfbnk', 'dgvf', 'rg'),
(11, 'tester', 'test@gmail.com', 'grg', 'regr'),
(12, 'Hrithik Roshan', 'hrithik@yahoo.com', 'jknjkknknkj', 'nkjf'),
(13, 'Hrithik Roshan', 'hrithik@yahoo.com', 'jknjkknknkj', 'nkjf'),
(14, 'Hrithik Roshan', 'hrithik@yahoo.com', 'hbjh', 'jknkj'),
(15, 'Hrithik Roshan', 'hrithik@yahoo.com', 'hbjh', 'jknkj'),
(16, 'testerq', 'tester@besterqq', 'jnkj', 'hmbjh\r\n'),
(17, 'testerq', 'tester@besterqq', 'jnkj', 'hmbjh\r\n'),
(18, 'testerq', 'tester@besterqq', 'jnkj', 'hmbjh\r\n'),
(19, 'testerq', 'tester@besterqq', 'jnkj', 'hmbjh\r\n'),
(20, 'jnkj', 'jknjkn@vjrsngkj', 'jkvnfdjk', 'jnvjkfdn'),
(21, 'fdsjhb', 'vjnfk@dskfbnk', 'hibi', 'jeew k'),
(22, 'njbj', 'gfb@jdfnjrn', 'db', 'tb'),
(23, 'njbj', 'gfb@jdfnjrn', 'db', 'tb'),
(24, 'njbj', 'gfb@jdfnjrn', 'db', 'tb'),
(25, 'njbj', 'gfb@jdfnjrn', 'db', 'tb'),
(26, 'njbj', 'gfb@jdfnjrn', 'db', 'tb'),
(27, 'njbj', 'gfb@jdfnjrn', 'db', 'tb'),
(28, 'njbj', 'gfb@jdfnjrn', 'db', 'tb'),
(29, 'njbj', 'gfb@jdfnjrn', 'db', 'tb'),
(30, 'njbj', 'gfb@jdfnjrn', 'db', 'tb'),
(31, 'kjdsnskd', 'gfb@jdfnjrn', 'db', 'tb'),
(32, 'Raj Ghadi', 'rajghadi1@gmail.com', 'trh', 'htr'),
(33, 'jadoo', 'jadoo@gmail.com', 'jaddoo', 'kdnck'),
(34, 'Raj Ghadi', 'rajghadi1@gmail.com', 'jrngkj', 'jnvjks');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `subject` varchar(30) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `dob` date DEFAULT NULL,
  `mobile` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `blood` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `dob`, `mobile`, `blood`) VALUES
(1, 'shrejay', 'itshre@gmail.com', '123', '2000-07-10', '', ''),
(2, 'tester2', 'test2@gmail.com', '000', '2021-12-15', '', ''),
(3, 'virat', 'virat@hh.com', '789', '2021-12-16', '', ''),
(4, 'john', 'j@gma.com', 'fgfg', '2021-12-07', '', ''),
(5, 'j', 'j@frg', 'defe', '2021-12-02', '', ''),
(6, 'Hrithik Roshan', 'hrithik@yahoo.com', 'jadoo', '2010-06-17', '', ''),
(7, 'Raj Ghadi', 'rajghadi1@gmail.com', '1410', '2000-10-14', '', ''),
(8, 'jadoo', 'jadoo@gmail.com', 'jadoo', '2021-12-15', '', ''),
(9, 'tester', 'test@gmail.com', '159', '2021-12-30', '12312312', 'A-');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
