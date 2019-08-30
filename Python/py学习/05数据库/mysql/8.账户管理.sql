
查看 mysql 初始的密码策略
show variables like 'validate_password%';

修改
set global validate_password_length=4;

set global validate_password_policy=LOW;




账户管理
使用user表
use mysql;

desc user;

查看用户
select user,host,authentication_string from user;

创建账户
grant 权限名称 on 数据库 to '用户名'@'访问主机' identified by '密码';

grant select on 表.* to 'liu'@'localhost' identified by '123456';
-- 查询权限select
-- 全部权限all privileges
-- 本地localhost 远程%

修改密码
    update mysql.user set authentication_string=password('新密码') where user='用户名';
update mysql.user set authentication_string=password('新密码') where user='root' and Host ='localhost';
ALTER mysql.user 'root'@'localhost' IDENTIFIED BY '新密码';


删除帐号root
drop user '用户名'@'主机';

远程连接
注释 vim /etc/mysql/mysql.conf.d/mysqld.cnf +43里面的bind-addr = 127.0.0.1  # 43行
mysql -uXXX -pXXX -h192.168.*.* -p3306

刷新权限
flush privileges;


