from django.db import models

# Create your models here.


class BookInfo(models.Model):

    # CharField是一个字符串，max_length指定字符串最大长度
    btitle = models.CharField(max_length=20)

    # DateField 是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        # 返回书名
        return self.btitle






class HeroInfo(models.Model):

    # 英雄名称
    hname = models.CharField(max_length=20)

    # 性别默认男 False男
    hgender = models.BooleanField(default=False)

    # 备注
    hcomment = models.CharField(max_length=128)

    # 建立图书类和英雄类一对多关系
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        # 返回书名
        return self.hname

