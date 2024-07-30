-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2024 at 10:15 AM
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
-- Database: `coba_4`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `no_tlp` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `nama`, `no_tlp`, `email`, `password`, `alamat`) VALUES
(1, 'WATI', '090909909', 'wati@gmail.com', '1234', 'Jl. Suka Rajin'),
(2, 'udin', '09090900', 'udin@gmail.com', '1234567', 'jl. suka megawati'),
(3, 'Budi ', '0090909090909', 'budi@gmail.com', '1234', 'jl. suka -suka '),
(4, 'hamzah', '200202020', 'hamzah@gmail.com', '11', 'jl. cikutra lama'),
(5, 'Namira', '082119303457', 'namira@gmail.com', '1234', 'jl. Cihanjuang ');

-- --------------------------------------------------------

--
-- Table structure for table `pengunjung`
--

CREATE TABLE `pengunjung` (
  `id_pelanggan` int(11) NOT NULL,
  `nama_pelanggan` varchar(50) NOT NULL,
  `no_tlp` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pengunjung`
--

INSERT INTO `pengunjung` (`id_pelanggan`, `nama_pelanggan`, `no_tlp`, `email`, `password`, `alamat`) VALUES
(1, 'WATI', '080808080', 'wati@gmail.com', '11', 'jl.suka-suka'),
(2, 'Yusron', '020202020', 'yusron@gmail.com', '12', 'jl . suka della'),
(3, 'Hamzah', '099909090', 'hamzah@gmail.com', '11', 'jl. suka membaca'),
(4, 'iqbal', '2020200202', 'iqbal@gmail.com', '13', 'jl.suka -suka'),
(5, 'budi', '09909090', 'budi@gmail.com', '11', 'jl. suka -suka '),
(6, 'nomnom', '08088080', 'nomnom@gmail.com', '11', 'jl. suka -suka '),
(7, 'Budi ', '00999090', 'amin@gmail,com', '123', 'jl , suka -suka'),
(8, 'erik', '09090909', 'erik@gmail.com', '11', 'jl.suka-suka'),
(9, 'hamzah.s', '080848305808', 'banglehamzah@gmail.com', '12', 'vhvvg');

-- --------------------------------------------------------

--
-- Table structure for table `produk`
--

CREATE TABLE `produk` (
  `id_produk` int(11) NOT NULL,
  `jenis_tas` varchar(50) NOT NULL,
  `merk_tas` varchar(50) NOT NULL,
  `harga` int(11) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `produk`
--

INSERT INTO `produk` (`id_produk`, `jenis_tas`, `merk_tas`, `harga`, `stock`) VALUES
(1, 'selempang', 'Eiger', 250000, 7),
(2, 'Koper', 'Eiger', 250000, 8),
(3, 'Tas Olahraga', 'Nike', 250000, 9),
(4, 'Ransel (Backpack)', 'Eiger', 150000, 10),
(5, 'Tas Laptop', 'Carbon', 100000, 10);

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `id_pengunjung` int(11) NOT NULL,
  `id_produk` int(11) NOT NULL,
  `jumlah_barang` int(11) NOT NULL,
  `total_harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id_transaksi`, `id_pengunjung`, `id_produk`, `jumlah_barang`, `total_harga`) VALUES
(1, 3, 1, 1, 250000),
(3, 4, 2, 2, 500000),
(4, 5, 2, 2, 500000),
(5, 2, 2, 6, 1500000),
(6, 3, 3, 1, 250000),
(7, 2, 3, 2, 500000),
(8, 1, 1, 3, 750000),
(9, 1, 1, 1, 0),
(10, 8, 2, 2, 500000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `pengunjung`
--
ALTER TABLE `pengunjung`
  ADD PRIMARY KEY (`id_pelanggan`);

--
-- Indexes for table `produk`
--
ALTER TABLE `produk`
  ADD PRIMARY KEY (`id_produk`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_pengunjung` (`id_pengunjung`,`id_produk`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `pengunjung`
--
ALTER TABLE `pengunjung`
  MODIFY `id_pelanggan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `produk`
--
ALTER TABLE `produk`
  MODIFY `id_produk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
