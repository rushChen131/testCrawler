CREATE DATABASE `pic` /*!40100 DEFAULT CHARACTER SET utf8 */ ;

CREATE DATABASE `taobao` /*!40100 DEFAULT CHARACTER SET utf8 */ ;

CREATE TABLE `t_taobao_search` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `html_url` VARCHAR(200) DEFAULT NULL COMMENT '当前页面url',
  `img_url` varchar(200) COLLATE utf8_bin DEFAULT NULL COMMENT '图片url',
  `img_path` varchar(100) COLLATE utf8_bin DEFAULT NULL COMMENT '图片本地路径',
  `link` varchar(200) COLLATE utf8_bin DEFAULT NULL COMMENT '索引指向url',
  `user_name` varchar(50) COLLATE utf8_bin DEFAULT NULL COMMENT '商家名',
  `title` varchar(200) COLLATE utf8_bin DEFAULT NULL COMMENT '商品名',
  `sales` bigint(15) COLLATE utf8_bin DEFAULT NULL COMMENT '销量',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='淘宝搜索页';



