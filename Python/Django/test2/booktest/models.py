from django.db import models
# Create your models here.

class BookInfoManager(models.Manager): # 图书模型管理器类
    def all(self): # 改变查询的结果集
        books = super().all() # 调用父类的all,获取所有数据
        books = books.filter(isDelete=False) # 对数据进行过滤
        return books # 返回books


    def create_book(self, btitle, dpub_date): # 添加额外的方法
        '''
        使用方法：
        BookInfo.book.create('test2','2013-05-06')

        不写create_book可以用下面的create来建立，必须指定传入的参数，效果一样

        BookInfo.book.create(btitle='test3',dpub_date='2013-05-06')

        '''
        model_class = self.model # 创建一个图书对象
        book = model_class() # 这个能自动获取输入时候的类名
        book.btitle = btitle
        book.dpub_date = dpub_date
        book.save()
        return book # 返回obj

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20) #名称
    # bprice = models.DecimalField(max_digits=10, decimal_places=2) # 价格最大位数10，小数点为2
    dpub_date = models.DateField() # 出版日期
    bread = models.IntegerField(default=0)  # 阅读量
    bcomment = models.IntegerField(default=0) # 评论量
    isDelete = models.BooleanField(default=False) # 删除标记

    # book = BookInfoManager() # 添加自定义管理器


    class Meta: # 类名和变量写法是固定的
        '''
        元类，改变应用名的时候变成booktest2，数据库里面，不再是booktest_bookinfo，变成booktest2_bookinfo，但是数据库不会更改，所以使用这个
        '''
        db_table = 'bookinfo' # 指定模型类对应的表名，数据库表


class HereInfo(models.Model):
    hname = models.CharField(max_length=20) # 英雄名
    hgender = models.BooleanField(default=False) # 性别
    hcomment = models.CharField(max_length=20) # 备注
    isDelete = models.BooleanField(default=False)  # 删除标记

    hbook = models.ForeignKey('bookInfo') # 关联属性 一对多关系 定义在多的类中

    # hbook = models.ManyToManyField('bookInfo') # 关联属性 多对多关系
    #
    # hbook = models.OneToOneField('bookInfo') # 一对一关系
