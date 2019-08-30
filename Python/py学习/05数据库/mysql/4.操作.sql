-- 向表中插入数据
insert into 表(标题) values...;
insert into 表 values(0, "..."), (0, "...")
insert into 表(标题) select(查询);

    -- 插入文件数据
    --cd 文件目录，登录mysql -u，切换到数据库
    source xxx.sql


-- 表1的字段1对应表2的字段2
-- 表1的字段1更改成表2字段1
update 表1 inner join 表2 on 表1.字段1=表2.字段2 set 表1.字段1=表2.字段1;


-- 添加外键约束
-- 表1字段和表2字段产生约束
alter table 表1 add foreign key (字段) references 表2(字段); --有冲突会报错，先删除


-- 取消外键约束
-- 先获取外键约束名称
show create table 表;
-- 获取后根据名称来删除外键约束
alter table 表 drop foreign key 外键名称;