-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 2021 年 04 月 10 日 13:09
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
-- 資料庫： `footlocker`
--

-- --------------------------------------------------------

--
-- 資料表結構 `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_email` varchar(100) NOT NULL,
  `admin_password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_email`, `admin_password`) VALUES
(1, 'admin@gmail.com', '1234');

-- --------------------------------------------------------

--
-- 資料表結構 `cart`
--

CREATE TABLE `cart` (
  `cart_id` int(8) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `product_id` int(8) DEFAULT NULL,
  `size` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `customers`
--

CREATE TABLE `customers` (
  `user_id` int(11) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone_no` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `customers`
--

INSERT INTO `customers` (`user_id`, `username`, `email`, `address`, `phone_no`, `password`) VALUES
(1, 'Tony', 'tony@gmail.com', 'Hong Kong', '12345678', '123'),
(2, 'chan', NULL, NULL, NULL, '1234');

-- --------------------------------------------------------

--
-- 資料表結構 `inqirty`
--

CREATE TABLE `inqirty` (
  `inqirty_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `question` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `inqirty`
--

INSERT INTO `inqirty` (`inqirty_id`, `name`, `email`, `question`) VALUES
(1, 'tony', 'tony@gmail.com', 'Hello!!!!!!!!!!!!!');

-- --------------------------------------------------------

--
-- 資料表結構 `orders`
--

CREATE TABLE `orders` (
  `order_id` int(8) NOT NULL,
  `username` varchar(8) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `totalprice` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `orders`
--

INSERT INTO `orders` (`order_id`, `username`, `date`, `totalprice`, `status`) VALUES
(1, 'tony', '2021-03-16', '1099', 'Payment Completed');

-- --------------------------------------------------------

--
-- 資料表結構 `order_detail`
--

CREATE TABLE `order_detail` (
  `id` int(8) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `product_id` int(8) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `order_id` int(8) DEFAULT NULL,
  `size` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `order_detail`
--

INSERT INTO `order_detail` (`id`, `username`, `product_id`, `status`, `order_id`, `size`) VALUES
(5, 'tony', 14, 'Payment Completed', 1, '40'),
(6, 'tony', 5, 'Payment Completed', 2, '36'),
(7, 'tony', 13, 'Payment Completed', 3, '43'),
(8, 'tony', 14, 'Payment Completed', 4, '40');

-- --------------------------------------------------------

--
-- 資料表結構 `products`
--

CREATE TABLE `products` (
  `item_no` int(8) NOT NULL,
  `item_type` varchar(100) DEFAULT NULL,
  `item` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `size` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `products`
--

INSERT INTO `products` (`item_no`, `item_type`, `item`, `price`, `size`, `image`) VALUES
(1, 'men', 'JORDAN MA2 SP', '1099', '40,41,42,43', 'product-1.png'),
(2, 'men', 'AIR JORDAN XXXV PF', '1499', '40,41,42,43', 'product-2.png'),
(3, 'men', 'NIKE AIR FORCE 1\'07LV8', '849', '40,41,42,43', 'product-3.png'),
(4, 'men', 'NIKE AIR ZOOM TEMPO NEXT% FK', '1099', '40,41,42,43', 'product-4.png'),
(5, 'women', 'NIKE DAYBREAK', '699', '36,37,38,39', 'product-5.png'),
(6, 'women', 'NIKE DBREAL-TYPE', '749', '36,37,38,39', 'product-6.png'),
(7, 'women', 'NIKE VISTA LITE', '599', '36,37,38,39', 'product-7.png'),
(8, 'women', 'NIKE AIR ZOOM TEMPO NEXT% FK', '1599', '36,37,38,39', 'product-8.png'),
(9, 'kids', 'NIKE AIR MAX 270RT (PS)', '489', '28,29,30,31', 'product-9.png'),
(10, 'kids', 'NIKE AIR MAX 2090 SP (PS)', '869', '28,29,30,31', 'product-10.png'),
(11, 'kids', 'NIKE DUNK HIGH SP (PS)', '599', '28,29,30,31', 'product-11.png'),
(12, 'kids', 'NIKE CORTEZ BASIC SL (PSV)', '469', '28,29,30,31', 'product-12.png'),
(13, 'newseason', 'NIKE AIR MAX VIVA', '999', '40,41,42,43', 'product-13.png'),
(14, 'newseason', 'JORDAN MA2 SP', '1099', '40,41,42,43', 'product-14.png'),
(15, 'newseason', 'NIKE DUNK LOW SP', '799', '40,41,42,43', 'product-15.png'),
(16, 'newseason', 'JORDAN DELTA MID', '1199', '40,41,42,43', 'product-16.png');

-- --------------------------------------------------------

--
-- 資料表結構 `replenishment`
--

CREATE TABLE `replenishment` (
  `replen_id` int(11) NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `item_type` varchar(100) NOT NULL,
  `supply_demand` varchar(100) NOT NULL,
  `shop` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL DEFAULT 'confirming'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `replenishment`
--

INSERT INTO `replenishment` (`replen_id`, `item_name`, `item_type`, `supply_demand`, `shop`, `status`) VALUES
(7, 'NIKE AIR ZOOM TEMPO NEXT% FK', 'women', '200', 'FootLocker', 'Order received'),
(8, 'NIKE DUNK HIGH SP (PS)', 'kids', '40', 'FootLocker', 'Order received'),
(9, 'NIKE AIR MAX VIVA', 'newseason', '500', 'FootLocker', 'Order received'),
(10, 'NIKE AIR MAX VIVA', 'newseason', '500', 'FootLocker', 'Order received'),
(11, 'NIKE DBREAL-TYPE', 'women', '50', 'FootLocker', 'Order received'),
(12, 'NIKE VISTA LITE', 'women', '200', 'FootLocker', 'Order received'),
(13, 'NIKE AIR ZOOM TEMPO NEXT% FK', 'women', '200', 'FootLocker', 'Order received'),
(14, 'NIKE DBREAL-TYPE', 'women', '100', 'footlocker', 'Order received');

-- --------------------------------------------------------

--
-- 資料表結構 `warehouse`
--

CREATE TABLE `warehouse` (
  `item_no` int(8) NOT NULL,
  `item` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `totalstock` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `warehouse`
--

INSERT INTO `warehouse` (`item_no`, `item`, `type`, `totalstock`) VALUES
(1, 'JORDAN MA2 SP', 'men', '100'),
(2, 'AIR JORDAN XXXV PF', 'men', '100'),
(3, 'NIKE AIR FORCE 1\'07LV8', 'men', '100'),
(4, 'NIKE AIR ZOOM TEMPO NEXT% FK', 'men', '100'),
(5, 'NIKE DAYBREAK', 'women', '100'),
(6, 'NIKE DBREAL-TYPE', 'women', '0'),
(7, 'NIKE VISTA LITE', 'women', '0'),
(8, 'NIKE AIR ZOOM TEMPO NEXT% FK', 'women', '0'),
(9, 'NIKE AIR MAX 270RT (PS)', 'kids', '100'),
(10, 'NIKE AIR MAX 2090 SP (PS)', 'kids', '50'),
(11, 'NIKE DUNK HIGH SP (PS)', 'kids', '0'),
(12, 'NIKE CORTEZ BASIC SL (PSV)', 'kids', '50'),
(13, 'NIKE AIR MAX VIVA', 'newseason', '0'),
(14, 'JORDAN MA2 SP', 'newseason', '100'),
(15, 'NIKE DUNK LOW SP', 'newseason', '100'),
(16, 'JORDAN DELTA MID', 'newseason', '100');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- 資料表索引 `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cart_id`);

--
-- 資料表索引 `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`user_id`);

--
-- 資料表索引 `inqirty`
--
ALTER TABLE `inqirty`
  ADD PRIMARY KEY (`inqirty_id`);

--
-- 資料表索引 `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`);

--
-- 資料表索引 `order_detail`
--
ALTER TABLE `order_detail`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`item_no`);

--
-- 資料表索引 `replenishment`
--
ALTER TABLE `replenishment`
  ADD PRIMARY KEY (`replen_id`);

--
-- 資料表索引 `warehouse`
--
ALTER TABLE `warehouse`
  ADD PRIMARY KEY (`item_no`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `cart`
--
ALTER TABLE `cart`
  MODIFY `cart_id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `customers`
--
ALTER TABLE `customers`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `inqirty`
--
ALTER TABLE `inqirty`
  MODIFY `inqirty_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `order_detail`
--
ALTER TABLE `order_detail`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `products`
--
ALTER TABLE `products`
  MODIFY `item_no` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `replenishment`
--
ALTER TABLE `replenishment`
  MODIFY `replen_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `warehouse`
--
ALTER TABLE `warehouse`
  MODIFY `item_no` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
