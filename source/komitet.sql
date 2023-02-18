-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Окт 26 2022 г., 01:52
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
(20, '620712601', NULL),
(26, '1432262023', NULL),
(31, '811376722', NULL),
(32, '1387992714', NULL),
(33, '5331959203', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `events`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text DEFAULT NULL,
  `e_date` datetime NOT NULL,
  `image` text DEFAULT NULL,
  `locate` text DEFAULT NULL,
  `tags` text DEFAULT NULL,
  `web_source` text DEFAULT NULL,
  `clmns` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `events`
--

INSERT INTO `events` (`id`, `name`, `description`, `e_date`, `image`, `locate`, `tags`, `web_source`, `clmns`) VALUES
(115, 'ЧтоГдеКогда', '«Что? Где? Когда?», и главное зачем? \nЗатем, чтобы проверить себя и своих друзей в области познания мира!', '2022-11-18 23:59:00', 'AgACAgIAAxkBAAIWlGNW-ciAyRSP5X9-LiDdlrIvgiHrAAKexTEbNF-4Slveoo8Y_o-yAQADAgADcwADKgQ', 'Внешнее', '0', '0', NULL),
(116, 'Чеееел', 'Опа нихуя', '2021-08-19 18:00:00', 'AgACAgIAAxkBAAIWwWNW-ysVdXGxdgG9P2z0TU9_SsvoAAKCxjEbV1W4Sh7MyOL5t-1bAQADAgADcwADKgQ', 'Внутреннее', '0', '0', NULL),
(117, 'Олеся стреляет пау пау', 'Олеся стреляет вуц пау пау, очень весело', '2022-11-12 20:00:00', 'AgACAgIAAxkBAAIXFmNW_HqK2_PQD_ixinCFA3K8JaA_AAKcvTEbKO24SjhX8frJqkEdAQADAgADcwADKgQ', 'Внутреннее', '0', 'https://www.youtube.com/', NULL),
(118, 'Вуцвуцвуц', 'Мы боги, аееее', '2023-11-12 14:00:00', 'AgACAgIAAxkBAAIXKGNW_Iqp1Q0MM-ACn33Nca8gKsuMAAKuxTEbNF-4SiJ4Jn4gav6TAQADAgADcwADKgQ', 'Внешнее', '0', '0', NULL),
(119, 'Кб-карш', 'Едем в КБ на карше', '2025-01-18 19:00:00', 'AgACAgIAAxkBAAIXS2NW_JulMyPSSTrGTHt8QuSIocYOAAKHxjEbV1W4SigK_pq1DlXCAQADAgADcwADKgQ', 'Внутреннее', '0', 'https://www.gismeteo.ru/weather-sankt-peterburg-4079/', NULL),
(121, 'Крысоловы', 'Ищем , ищем, пипипи', '2022-11-11 11:11:00', 'AgACAgIAAxkBAAIXi2NW_Pm7bazXwlzG-ee_BDmGFyQZAAK1xTEbNF-4Sj6mED5xEAsOAQADAgADcwADKgQ', 'Внутреннее', '0', '0', NULL),
(122, 'Ваня дрочит письку', '24/7', '2027-06-18 15:00:00', 'AgACAgIAAxkBAAIXj2NW_QwFPn3JnvJtOxfLtUn-dmnYAAKKxjEbV1W4ShRdmLNW5FvVAQADAgADcwADKgQ', 'Внешнее', '0', '0', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `inside_subs`
--

CREATE TABLE `inside_subs` (
  `id` int(11) NOT NULL,
  `login` bigint(20) NOT NULL,
  `name` text NOT NULL,
  `photo` text NOT NULL,
  `type` text DEFAULT NULL,
  `target` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `inside_subs`
--

INSERT INTO `inside_subs` (`id`, `login`, `name`, `photo`, `type`, `target`) VALUES
(54, 1432262023, 'Николай Петрович', 'AgACAgIAAxkBAAIUmGNVnfsY-lhfWw4sdWHHybI-JhiaAAJswjEbxoqoSo0GnOAVT58UAQADAgADcwADKgQ', 'razrab', '0'),
(61, 811376722, 'Воронин Иван', 'AgACAgIAAxkBAAIWY2NW-OROOdrefH0OupOucsTolkmEAAKaxTEbNF-4Sk6UNbZ3sbsjAQADAgADcwADKgQ', 'smm', '0'),
(62, 1387992714, 'Абобус Олеся Дмитриевна', 'AgACAgIAAxkBAAIYCmNW_tMfFSEkA3JGHJfRVpVs3JOGAAJrvDEbTDCxSlor7uAyW37YAQADAgADcwADKgQ', 'smm', '0');

-- --------------------------------------------------------

--
-- Структура таблицы `komitet_users`
--

CREATE TABLE `komitet_users` (
  `id` bigint(20) NOT NULL,
  `name` text NOT NULL,
  `image` text DEFAULT NULL,
  `description` text NOT NULL,
  `division` text NOT NULL,
  `status` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `filling` text NOT NULL,
  `division` text NOT NULL,
  `e_date` date NOT NULL,
  `joined` text DEFAULT NULL,
  `image` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `qq_list`
--

CREATE TABLE `qq_list` (
  `for_id` int(11) NOT NULL,
  `for_log` text DEFAULT NULL,
  `for_name` text DEFAULT NULL,
  `for_description` text DEFAULT NULL,
  `for_photo` text DEFAULT NULL,
  `for_birth` text DEFAULT NULL,
  `for_faculty` text DEFAULT NULL,
  `for_group` text DEFAULT NULL,
  `for_course` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `qq_list`
--

INSERT INTO `qq_list` (`for_id`, `for_log`, `for_name`, `for_description`, `for_photo`, `for_birth`, `for_faculty`, `for_group`, `for_course`) VALUES
(1, 'Пожалуйста, отправьте мне своё фото)', 'Ну давай же', NULL, 'Давай', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `sublist07`
--

CREATE TABLE `sublist07` (
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist08`
--

CREATE TABLE `sublist08` (
  `name` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist10`
--

CREATE TABLE `sublist10` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist94`
--

CREATE TABLE `sublist94` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist95`
--

CREATE TABLE `sublist95` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist97`
--

CREATE TABLE `sublist97` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist109`
--

CREATE TABLE `sublist109` (
  `name` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist113`
--

CREATE TABLE `sublist113` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `faculty` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist115`
--

CREATE TABLE `sublist115` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist116`
--

CREATE TABLE `sublist116` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist117`
--

CREATE TABLE `sublist117` (
  `log` int(11) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist118`
--

CREATE TABLE `sublist118` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist119`
--

CREATE TABLE `sublist119` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist120`
--

CREATE TABLE `sublist120` (
  `log` int(11) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist121`
--

CREATE TABLE `sublist121` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` text DEFAULT NULL,
  `BirthDate` text DEFAULT NULL,
  `faculty` text DEFAULT NULL,
  `group_` text DEFAULT NULL,
  `course` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `sublist122`
--

CREATE TABLE `sublist122` (
  `log` int(11) DEFAULT NULL,
  `name` text DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
-- Индексы таблицы `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `qq_list`
--
ALTER TABLE `qq_list`
  ADD PRIMARY KEY (`for_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `admin`
--
ALTER TABLE `admin`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT для таблицы `events`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123;

--
-- AUTO_INCREMENT для таблицы `inside_subs`
--
ALTER TABLE `inside_subs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT для таблицы `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
