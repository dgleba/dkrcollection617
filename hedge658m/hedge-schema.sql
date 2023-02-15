-- Adminer 4.7.9 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `Authors`;
CREATE TABLE `Authors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `color` varchar(255) DEFAULT NULL,
  `noteId` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `userId` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `createdAt` datetime DEFAULT NULL,
  `updatedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Author_note_fkey` (`noteId`),
  KEY `Author_user_fkey` (`userId`),
  CONSTRAINT `Author_note_fkey` FOREIGN KEY (`noteId`) REFERENCES `Notes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Author_user_fkey` FOREIGN KEY (`userId`) REFERENCES `Users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `Notes`;
CREATE TABLE `Notes` (
  `id` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `ownerId` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `content` longtext DEFAULT NULL,
  `title` text DEFAULT NULL,
  `createdAt` datetime DEFAULT NULL,
  `updatedAt` datetime DEFAULT NULL,
  `shortid` varchar(255) NOT NULL DEFAULT '0000000000',
  `permission` enum('freely','editable','limited','locked','protected','private') DEFAULT NULL,
  `viewcount` int(11) DEFAULT 0,
  `lastchangeuserId` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `lastchangeAt` datetime DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `savedAt` datetime DEFAULT NULL,
  `authorship` longtext DEFAULT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `notes_shortid` (`shortid`),
  KEY `notes_alias` (`alias`),
  KEY `Notes_owner_fkey` (`ownerId`),
  CONSTRAINT `Notes_owner_fkey` FOREIGN KEY (`ownerId`) REFERENCES `Users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `Notes` (`id`, `ownerId`, `content`, `title`, `createdAt`, `updatedAt`, `shortid`, `permission`, `viewcount`, `lastchangeuserId`, `lastchangeAt`, `alias`, `savedAt`, `authorship`, `deletedAt`) VALUES
('7bf3cd90-a187-4f39-9d82-e8af75529fb3',	NULL,	'2023-02-12_Sun_22.18-PM',	'Untitled',	'2023-02-13 03:18:46',	'2023-02-13 03:25:09',	'1Gbg-bNaB',	'freely',	0,	NULL,	'2023-02-13 03:18:53',	NULL,	'2023-02-13 03:25:09',	'[]',	NULL),
('9f0a13c6-b280-4404-891d-68aaff500fb2',	'98a44419-0f36-4a7b-a609-7d59f43760f1',	'=================================================\n\n2023-02-12_Sun_22.30-PM',	'Untitled',	'2023-02-13 03:30:31',	'2023-02-13 03:38:57',	'B78HIGo64',	'editable',	0,	'98a44419-0f36-4a7b-a609-7d59f43760f1',	'2023-02-13 03:30:39',	NULL,	'2023-02-13 03:38:56',	'[[\"98a44419-0f36-4a7b-a609-7d59f43760f1\",0,74,1676259037822,1676259039710]]',	NULL);

DROP TABLE IF EXISTS `Revisions`;
CREATE TABLE `Revisions` (
  `id` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `noteId` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `patch` longtext DEFAULT NULL,
  `lastContent` longtext DEFAULT NULL,
  `content` longtext DEFAULT NULL,
  `length` int(11) DEFAULT NULL,
  `createdAt` datetime DEFAULT NULL,
  `updatedAt` datetime DEFAULT NULL,
  `authorship` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Revisions_note_fkey` (`noteId`),
  CONSTRAINT `Revisions_note_fkey` FOREIGN KEY (`noteId`) REFERENCES `Notes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `SequelizeMeta`;
CREATE TABLE `SequelizeMeta` (
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


DROP TABLE IF EXISTS `Sessions`;
CREATE TABLE `Sessions` (
  `sid` varchar(36) NOT NULL,
  `expires` datetime DEFAULT NULL,
  `data` text DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `Temp`;
CREATE TABLE `Temp` (
  `id` varchar(255) NOT NULL,
  `date` text DEFAULT NULL,
  `createdAt` datetime DEFAULT NULL,
  `updatedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
  `id` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `profileid` varchar(255) DEFAULT NULL,
  `profile` text DEFAULT NULL,
  `history` longtext DEFAULT NULL,
  `createdAt` datetime DEFAULT NULL,
  `updatedAt` datetime DEFAULT NULL,
  `accessToken` text DEFAULT NULL,
  `refreshToken` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `password` text DEFAULT NULL,
  `deleteToken` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `profileid` (`profileid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- 2023-02-13 03:40:03
