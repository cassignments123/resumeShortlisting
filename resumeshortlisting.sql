-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Mar 23, 2022 at 12:58 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `resumeshortlisting`
--

-- --------------------------------------------------------

--
-- Table structure for table `jobposting`
--

CREATE TABLE `jobposting` (
  `id` int(10) NOT NULL,
  `company_id` int(10) NOT NULL,
  `c_name` varchar(25) NOT NULL,
  `skills` varchar(100) NOT NULL,
  `experience` int(10) NOT NULL,
  `education` varchar(50) NOT NULL,
  `city` text NOT NULL,
  `generated_link` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jobposting`
--

INSERT INTO `jobposting` (`id`, `company_id`, `c_name`, `skills`, `experience`, `education`, `city`, `generated_link`) VALUES
(1, 1, 'Infosys', 'Flask', 2, 'BE', 'Gandhinagar', 'www.Infosys/1/1'),
(2, 6, 'TCS', 'Javascript', 5, 'M.Tech', 'Ahmedabad', 'www.TCS/2/6'),
(3, 9, 'Echo', 'Ruby', 3, 'B.Tech', 'Mumbai', 'www.Echo/3/9'),
(4, 6, 'TCS', 'Java', 0, 'BE', 'Ahmedabad', 'www.TCS/4/6'),
(5, 10, 'Google', 'Machine Learning', 5, 'M.Tech', 'Bangalore', 'www.Google/5/10'),
(6, 11, 'Amazon', 'AWS', 2, 'B.Tech', 'Karnataka', 'www.Amazon/6/11'),
(7, 10, 'Google', 'Cloud', 2, 'BE', 'Ahmedabad', 'www.Google/7/1');

-- --------------------------------------------------------

--
-- Table structure for table `recruiter`
--

CREATE TABLE `recruiter` (
  `id` int(10) NOT NULL,
  `company_email` varchar(100) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recruiter`
--

INSERT INTO `recruiter` (`id`, `company_email`, `company_name`, `password`) VALUES
(1, 'prteu34@gmail.com', 'xyz', '12345678'),
(2, 'harjanihema52@gmail.com', 'abc', 'qwerty'),
(3, 'preetiharjani1382@gmail.com', 'food', 'food123'),
(4, 'prteu35@gmail.com', 'food@', 'food@123'),
(5, 'harjanihema55@gmail.com', 'wipro', '123preeti'),
(6, 'tcs.hr@gmail.com', 'TCS', 'tcs.hr12'),
(8, 'infosys.hr@gmail.com', 'Infosys', 'info@hr1'),
(9, 'echohr@yahoo.com', 'Echo', 'echo1@hr'),
(10, 'google@hotmail.com', 'Google', 'google1@hire'),
(11, 'hr@amazon.in', 'Amazon', 'hire@amazon');

-- --------------------------------------------------------

--
-- Table structure for table `resume_details`
--

CREATE TABLE `resume_details` (
  `id` int(10) NOT NULL,
  `job_id` int(10) NOT NULL,
  `template_id` int(10) NOT NULL,
  `name` text NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `contact_number` int(12) NOT NULL,
  `address` varchar(100) NOT NULL,
  `title` varchar(50) NOT NULL,
  `skills` varchar(100) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `position` varchar(50) NOT NULL,
  `worked_from` date NOT NULL,
  `worked_to` date NOT NULL,
  `description` varchar(100) NOT NULL,
  `project_title` varchar(50) NOT NULL,
  `project_description` varchar(150) NOT NULL,
  `tech_used` varchar(100) NOT NULL,
  `education` varchar(80) NOT NULL,
  `languages_known` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resume_details`
--

INSERT INTO `resume_details` (`id`, `job_id`, `template_id`, `name`, `dob`, `email`, `contact_number`, `address`, `title`, `skills`, `company_name`, `position`, `worked_from`, `worked_to`, `description`, `project_title`, `project_description`, `tech_used`, `education`, `languages_known`) VALUES
(1, 0, 1, 'Jay Patel', '2001-10-23', 'jayp12@gmail.com', 2147483647, '24,Sarthak Society,\r\nSector20,\r\nGandhinagar\r\n383826', 'PHP Developer', 'PHP', 'InfoTech', 'PHP Developer', '2020-02-26', '2021-11-24', 'I am an experienced joiner with well developed skills and experience in groundwork, concrete finishi', 'Hotel Management', 'Hotel Management System is a web-based application that allows the hotel manager to handle all hotel activities online. Interactive GUI and the abilit', 'PHP,HTML,CSS', 'B.Tech', 'English'),
(2, 0, 1, 'Abhay Singh', '2001-06-10', 'abhay12@gmail.com', 2147483647, '9,Sanjay Bunglows,\r\nNaroda,\r\nAhmedabad\r\n384574', 'Python Developer', 'python', 'Tech Mahindra', 'Python Intern', '2020-04-08', '2021-11-05', 'I am an experienced joiner with well developed skills and experience in groundwork, concrete finishi', 'Hotel Management', 'Analyzed user needs and proposed design software solutions to meet them.\r\nSupporting testing operating systems-level software', 'Python,Flask,CSS,HTML', 'BE', 'English'),
(3, 0, 1, 'Ranveer Rathod', '2001-05-29', 'ranveer2001@gmail.com', 2147483647, '101,Green Flats,\r\nHansol,\r\nAhmedabad\r\n382475', 'IT Technician', 'Java', 'OpenXcel', 'Java Developer', '2021-02-08', '2021-10-05', 'Assisted in maintenance of software for engineering applications\r\nCommitted code to GIT/SVN and crea', 'Network packet sniffer', 'Network packet sniffer is a packet analyzer software that monitors all network traffic. The proposed project is implemented in Java programming langua', 'Java,Hibernate', 'BE', 'English');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jobposting`
--
ALTER TABLE `jobposting`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recruiter`
--
ALTER TABLE `recruiter`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `resume_details`
--
ALTER TABLE `resume_details`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jobposting`
--
ALTER TABLE `jobposting`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `recruiter`
--
ALTER TABLE `recruiter`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `resume_details`
--
ALTER TABLE `resume_details`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
