-- 数据库操作
    -- 显示sql版本
    select version();

    -- 查看所有数据库
    show databases;

    -- 创建数据库
    create database python charset=utf8;

    -- 查看创建的数据库语句
    show create database python;

    -- 查看当前使用的的数据库
    select database();

    -- 使用当前数据库
    use python;

    -- 删除数据库
    drop database python;




-- 数据表的操作
    -- 查看当前数据库中所有表
    show tables;

    -- 创建表
    -- auto_increment表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值
    -- create table 数据表名字(字段 类型 约束(, 字段 类型 约束));
    -- 创建classes表(id,name)
      create table xx(id int, name varchar(30));
      create table xx(id int primary key not null auto, name varchar(30));

    -- desc 数据表的名字;
    -- 查询数据表属性
     desc xxx;

    -- 创建students表(id、name、age、high、gender、cls_id)
      create table students (
          id int unsigned not null auto_increment primary key,
          name varchar(30),
          age tinyint unsigned default 0,
          high decimal(5,2),
          gender enum("男", "女", "中", "保密") default "保密",
          cls_id int unsigned
      );

          -- 添加数据
            insert into students values(0, "老王", 18, 188.88, "男", 0);
            insert into students (...) select ... from ...;
          -- 查看表
            select * from students;

    -- 创建classes表（id、name）
      create table classes(
          id int unsigned not null auto_increment,
          name
      );

      insert into classes values(0, "一二三")
      select * from classes;

    -- 查看表的创建语句
      show create table python

    -- 修改表-添加字段
      -- alter table 表名 add 列名 类型;
      alter table students add birthday datetime;


    -- 修改表-修改字段：不含重命名版
      -- alter table 表名 modify 列名 类型及约束;
      alter table students modify birthday date;

    -- 修改表-修改字段：重命名版
      after table 表名 change 原名 新名 类型及约束;
      after table students change birthday birth birth date default "2000-01-01"

    -- 修改表-删除字段
      -- after table 表名 drop 列名;
      after table students drop high;

    -- 删除表
      -- drop table 表名;
      drop table 数据表;





-- 增删改查(curd) 创建 Create 修改 Update 读取 Retrieve 删除 Delete

    -- 增加
        -- 全列插入
        -- insert (into) 表名 values(...)
        -- 主键字段 可以用 0 null default 来占位
        -- 向classes表中插入 一个班级
        insert into classes values(0, "java")

        -- 向students表插入 一个学生信息
        insert into students values(0, "小明", 20, "女", 1, "1994-12-03");
        insert into students values(null, "小张", 20, "女", 1, "1994-12-03");
        insert into students values(default, "小张", 20, "女", 1, "1994-12-03");

        -- 枚举中的下标从1开始 1--->"男" 2--->"女" 3--->"中性" 4--->"保密"
        insert into students values(default, "小张", 20, 1, 1, "1994-12-03");
        insert into students values(default, "小张", 20, 2, 1, "1994-12-03");

        -- 部分插入
        -- insert into 表名(列1, ...) values(值1, ...)
        insert into students (name, gender) values("小乔", 2)

        -- 多行插入
        insert into students (name, gender) values("小乔", 2), ("貂蝉", 2);
        insert into students values(default, "小张", 20, 4, 1, "1994-12-03"), (default, "小王", 20, 4, 1, "1994-12-03");


    -- 修改
        -- update 表名 set 列1=值1, 列2=值2... where 条件;
        -- 全改
        update students set gender=1;

        -- 改一个
        update students set gender=2 where id=3;
        update students set age=22,name="王者" where id=4;


    -- 删除
        -- 物理删除
        -- delete from 表名 where 条件;
        -- 删除整个数据表中的所有数据
        delete from students;
        delete from students where name="小明";
        -- 删了之后就不要再用 否则会出问题


        -- 逻辑删除
        -- 用一个字段来表示，这条信息是否已经不能再使用了
        -- 给students表添加一个is_delete字段 bit 类型
        -- alter table students add is_delete bit default 0;
        alter table students add is_delete bit default 0;
        -- update students set is_delete=1 where id=6;
        update students set is_delete=1 where id=6;


    -- 查询基本使用
        -- 查询所有列
        -- select * from 表名
        -- 表字段很多的话 查询很慢

        -- 指定条件查询
        select * from students where id>5;
        select * from students where id<10;
        select * from students where name="小明";


        -- 查询指定列
        -- select 列1，列2，... from 表名;
        select name, gender from students;


        -- 字段的顺序
        -- 可以使用as为列或表指定别名
        -- select 字段(as 别名), 字段(as 别名) from 数据表 where ...;
        select name as 姓名, gender as 性别 from students;
        select gender as 性别, name as 姓名 from students;
