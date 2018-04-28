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

 Date: 04/27/2018 10:39:12 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(8) CHARACTER SET utf8 NOT NULL,
  `password` varchar(32) NOT NULL,
  `headimg` varchar(400) CHARACTER SET utf8 NOT NULL,
  `introduce` varchar(60) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `user`
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES ('1', 'zjl', 'e10adc3949ba59abbe56e057f20f883e', 'http://192.168.1.104:5000/uploads/0031524663731.png', '这是简单的介绍,你懂的,哈哈哈哈,这是我的博客,前端用到了vue的各种技术,哈哈哈,dadaccccc');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
