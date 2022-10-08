-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Сен 19 2022 г., 18:33
-- Версия сервера: 10.3.22-MariaDB
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `komitet`
--

-- --------------------------------------------------------

--
-- Структура таблицы `admin`
--

CREATE TABLE `admin` (
  `id` bigint(20) NOT NULL,
  `login` text NOT NULL,
  `prjcts` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `admin`
--

INSERT INTO `admin` (`id`, `login`, `prjcts`) VALUES
(1, '1111', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `events`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text DEFAULT NULL,
  `e_date` datetime NOT NULL,
  `image` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `events`
--

INSERT INTO `events` (`id`, `name`, `description`, `e_date`, `image`) VALUES
(1, 'aax', 'asxasxaxax', '2022-11-15 22:00:00', 'fndnvflnv'),
(2, 'aax', 'asxasxaxax', '2022-11-15 22:00:00', 'fndnvflnv'),
(3, 'aax', 'asxasxaxax', '2022-11-05 22:00:00', 'fndnvflnv'),
(4, 'aaa', 'asas', '2022-12-09 12:00:00', 'azazaz'),
(5, 'aaa', 'asas', '2022-12-09 12:00:00', 'azazaz'),
(6, 'aaa', 'asas', '2022-08-09 12:00:00', 'azazaz'),
(7, 'Uu', 'Yy', '2022-11-14 22:00:00', 'AQADhL0xGw59QEl4'),
(8, 'Yy', 'Uu', '2022-11-14 22:00:00', 'AQADhL0xGw59QEl4'),
(9, 'Yy', 'Ii', '2022-11-14 22:00:00', 'AgACAgIAAxkBAAIBvWMndLqMnOjC68rvC82sD7P7g9pdAAKEvTEbDn1ASfZWloJpySKsAQADAgADcwADKQQ'),
(10, 'Yyy', 'Iii', '2022-11-14 22:00:00', 'AgACAgIAAxkBAAIBx2MndOSpULcjlo_yNr3BQEkDZ7esAAKEvTEbDn1ASfZWloJpySKsAQADAgADcwADKQQ'),
(11, 'Пример мероприятия', 'Очень веселое', '2022-11-14 22:00:00', '0'),
(12, 'Офлайн встреча комитета', 'Очень веселое мероприятие', '2022-09-24 16:00:00', 'AgACAgIAAxkBAAIB-GMndc0D2EP7y9Vp_ljV0VId9M-IAAKEvTEbDn1ASfZWloJpySKsAQADAgADcwADKQQ'),
(13, 'тестовое меро', 'тестовое меро', '2022-04-25 10:30:00', '0');

-- --------------------------------------------------------

--
-- Структура таблицы `inside_subs`
--

CREATE TABLE `inside_subs` (
  `id` int(11) NOT NULL,
  `login` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `inside_subs`
--

INSERT INTO `inside_subs` (`id`, `login`) VALUES
(1, 11),
(10, 1829820646);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `inside_subs`
--
ALTER TABLE `inside_subs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `admin`
--
ALTER TABLE `admin`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `events`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT для таблицы `inside_subs`
--
ALTER TABLE `inside_subs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
