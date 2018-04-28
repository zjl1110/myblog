/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50713
 Source Host           : localhost
 Source Database       : dbtest

 Target Server Type    : MySQL
 Target Server Version : 50713
 File Encoding         : utf-8

 Date: 04/27/2018 10:39:05 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `contenttype`
-- ----------------------------
DROP TABLE IF EXISTS `contenttype`;
CREATE TABLE `contenttype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(30) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `contenttype`
-- ----------------------------
BEGIN;
INSERT INTO `contenttype` VALUES ('1', '随笔'), ('3', '前端'), ('4', 'js'), ('5', 'css'), ('6', 'xxx'), ('7', 'ggg');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
