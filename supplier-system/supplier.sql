-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 2021 年 04 月 10 日 13:08
-- 伺服器版本： 10.4.14-MariaDB
-- PHP 版本： 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `supplier`
--

-- --------------------------------------------------------

--
-- 資料表結構 `inventory`
--

CREATE TABLE `inventory` (
  `item_no` int(8) NOT NULL,
  `item_type` varchar(100) DEFAULT NULL,
  `item` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `size` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `inventory`
--

INSERT INTO `inventory` (`item_no`, `item_type`, `item`, `price`, `size`) VALUES
(1, 'men', 'JORDAN MA2 SP', '1099', '40,41,42,43'),
(2, 'men', 'AIR JORDAN XXXV PF', '1499', '40,41,42,43'),
(3, 'men', 'NIKE AIR FORCE 1\'07LV8', '849', '40,41,42,43'),
(4, 'men', 'NIKE AIR ZOOM TEMPO NEXT% FK', '1099', '40,41,42,43'),
(5, 'women', 'NIKE DAYBREAK', '699', '36,37,38,39'),
(6, 'women', 'NIKE DBREAL-TYPE', '749', '36,37,38,39'),
(7, 'women', 'NIKE VISTA LITE', '599', '36,37,38,39'),
(8, 'women', 'NIKE AIR ZOOM TEMPO NEXT% FK', '1599', '36,37,38,39'),
(9, 'kids', 'NIKE AIR MAX 270RT (PS)', '489', '28,29,30,31'),
(10, 'kids', 'NIKE AIR MAX 2090 SP (PS)', '869', '28,29,30,31'),
(11, 'kids', 'NIKE DUNK HIGH SP (PS)', '599', '28,29,30,31'),
(12, 'kids', 'NIKE CORTEZ BASIC SL (PSV)', '469', '28,29,30,31'),
(13, 'newseason', 'NIKE AIR MAX VIVA', '999', '40,41,42,43'),
(14, 'newseason', 'JORDAN MA2 SP', '1099', '40,41,42,43'),
(15, 'newseason', 'NIKE DUNK LOW SP', '799', '40,41,42,43'),
(16, 'newseason', 'JORDAN DELTA MID', '1199', '40,41,42,43');

-- --------------------------------------------------------

--
-- 資料表結構 `invoice`
--

CREATE TABLE `invoice` (
  `invoice_no` int(50) NOT NULL,
  `order_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `reple_order`
--

CREATE TABLE `reple_order` (
  `id` int(8) NOT NULL,
  `item` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `supply_demand` varchar(100) NOT NULL,
  `shop` varchar(100) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `reple_order`
--

INSERT INTO `reple_order` (`id`, `item`, `type`, `supply_demand`, `shop`, `date`) VALUES
(1, 'JORDAN MA2 SP', 'men', '100', 'footloker', '2021-03-31');

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `user_id` int(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `user`
--

INSERT INTO `user` (`user_id`, `email`, `pwd`) VALUES
(1, 'admin@gmail.com', '123');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`item_no`);

--
-- 資料表索引 `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`invoice_no`);

--
-- 資料表索引 `reple_order`
--
ALTER TABLE `reple_order`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `inventory`
--
ALTER TABLE `inventory`
  MODIFY `item_no` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `invoice`
--
ALTER TABLE `invoice`
  MODIFY `invoice_no` int(50) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `reple_order`
--
ALTER TABLE `reple_order`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
