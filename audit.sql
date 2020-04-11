insert into port_ip_relation (port,ip,deleteflag) values (4444,'192.168.0.91',0);
insert into port_ip_relation (port,ip,deleteflag) values (4445,'192.168.0.91',0);
insert into port_ip_relation (port,ip,deleteflag) values (4446,'192.168.0.91',0);

CREATE TABLE `port_ip_relation` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `port` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '端口号',
  `ip` varchar(255) NOT NULL DEFAULT '' COMMENT 'ip',
  `deleteflag` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `createdt` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='port ip 关系表';

#执行实例的用户
CREATE USER 'struct_alter'@'10.20.4.%' IDENTIFIED BY 'struct_alter';
grant alter,select,insert,update,create,drop on *.* to 'struct_alter'@'10.20.4.%';

CREATE USER 'struct_alter'@'192.168.%' IDENTIFIED BY 'struct_alter';
grant alter,select,insert,update,create,drop on *.* to 'struct_alter'@'192.168.%';

#存放备份的用户
CREATE USER 'djyv4_rw'@'10.20.%' IDENTIFIED BY 'tfkj_secret';
grant alter,select,insert,update,create on *.* to 'djyv4_rw'@'10.20.%';

CREATE USER 'djyv4_rw'@'192.168.%' IDENTIFIED BY 'tfkj_secret';
grant alter,select,insert,update,create on *.* to 'djyv4_rw'@'192.168.%';
