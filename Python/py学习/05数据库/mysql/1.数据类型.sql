整数

  tinyint(m)	  1个字节  范围(-128~127)
  smallint(m)	  2个字节  范围(-32768~32767)
  mediumint(m)	3个字节  范围(-8388608~8388607)
  int(m)	      4个字节  范围(-2147483648~2147483647)
  bigint(m)	    8个字节  范围(+-9.22*10的18次方)

  后面跟 unsigned 则最大值翻倍 如 tinyint unsigned 的取值范围为(0~255)


浮点型

  float(m,d)	单精度浮点型    8位精度(4字节)     m总个数d小数位
  double(m,d)	双精度浮点型    16位精度(8字节)    m总个数d小数位


定点数

  decimal(m,d)  一共有m位数 d位小数 (10,3)一共有10位数 3位小数 7位整数


字符串

  char(n)	    固定长度 最多255个字符
  varchar(n)	可变长度 最多65535个字符
  tinytext	  可变长度 最多255个字符
  text	      可变长度 最多65535个字符
  mediumtext	可变长度 最多2的24次方-1个字符
  longtext	  可变长度 最多2的32次方-1个字符


二进制数据

  bit 一比特 0,1


日期时间类型

  date	    日期 '2008-12-2'
  time	    时间 '12:25:36'
  datetime	日期时间 '2008-12-2 22:06:44'
  timestamp	自动存储记录修改时间


属性/约束

  null 	              数据列可包含NULL值
  not null 	          数据列不允许包含NULL值
  default 	          默认值
  primary key         主键
  auto_increment      自动递增	适用于整数类型
  unsigned	          无符号
  unique              唯一此字段
  character set name	指定一个字符集

