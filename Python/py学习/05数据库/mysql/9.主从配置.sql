
主从配置


备份数据库
mysqldump -uroot -p 数据库名 > xxx.sql;

恢复数据库
创建一个新的数据库
mysql -uroot -p 新数据库名 < python.sql

在ubuntu上执行备份
mysqldump -uroot -pmysql --all-databases --lock-all-tables > ~/master_db.sql

还原
mysql -uroot -pmysql < master_db.sql





配置主服务器
打开 sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
去除#  server-id =1 和从服务器不能一样
       log...
重启服务器
sudo service mysql restart

从服务器84行不用开 ID和主服务器不能一样

登入主服务器
mysql -uroot -pmysql
GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%' identified by 'slave'; --创建一个slave用户内网登录，密码slave

刷新权限
FLUSH PRIVILEGES;

获取主服务器的二进制日志信息
SHOW MASTER STATUS;

进入从服务器输入
change master to master_host='主服务器IP', master_user='slave', master_password='slave',master_log_file='mysql数据库-bin.000006', master_log_pos=590;

检查 从服务器输入  slave_IO_Running:YES下面的也是YES 表示成功
show slave status \G;
