-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2024 at 03:36 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411205`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_karywan`
--

CREATE TABLE `data_karywan` (
  `id_karyawan` int(11) NOT NULL,
  `Nama_Karyawan` varchar(25) NOT NULL,
  `id_Jabatan` int(11) NOT NULL,
  `Gaji` int(11) NOT NULL,
  `sandi` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_karywan`
--

INSERT INTO `data_karywan` (`id_karyawan`, `Nama_Karyawan`, `id_Jabatan`, `Gaji`, `sandi`) VALUES
(1, 'febi', 6, 25000000, '12rt'),
(3, 'WulanDini', 6, 5000000, '12rt'),
(4, 'velen shinta', 7, 25000000, '12rt'),
(5, 'Nurma', 9, 2000000, '34356'),
(6, 'karina', 6, 5000000, 'd3443');

-- --------------------------------------------------------

--
-- Table structure for table `jabatan`
--

CREATE TABLE `jabatan` (
  `id_jabatan` int(11) NOT NULL,
  `Nama_jabatan` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jabatan`
--

INSERT INTO `jabatan` (`id_jabatan`, `Nama_jabatan`) VALUES
(5, 'manager'),
(6, 'Staf Kebersihan'),
(7, 'HRD'),
(8, 'Satpam'),
(9, 'Staf');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_karywan`
--
ALTER TABLE `data_karywan`
  ADD PRIMARY KEY (`id_karyawan`),
  ADD KEY `id_Jabatan` (`id_Jabatan`);

--
-- Indexes for table `jabatan`
--
ALTER TABLE `jabatan`
  ADD PRIMARY KEY (`id_jabatan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_karywan`
--
ALTER TABLE `data_karywan`
  MODIFY `id_karyawan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `jabatan`
--
ALTER TABLE `jabatan`
  MODIFY `id_jabatan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `data_karywan`
--
ALTER TABLE `data_karywan`
  ADD CONSTRAINT `data_karywan_ibfk_1` FOREIGN KEY (`id_Jabatan`) REFERENCES `jabatan` (`id_jabatan`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
