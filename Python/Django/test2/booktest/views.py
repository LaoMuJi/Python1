from django.shortcuts import render,redirect # 导入重定向函数redirect 简写 子
from .models import BookInfo
from datetime import date


# from django.http import HttpResponse,HttpResponseRedirect # 重定向函数 复杂写 父
# Create your views here.

def index(request):

    # 查询图书的信息
    books = BookInfo.objects.all()

    return render(request, 'booktest/index.html', {'books':books})

def create(request):

    # 创建一个bookinfo对象
    b = BookInfo()
    b.btitle = '984514'
    b.dpub_date = date(2000,1,1)
    b.save() # 插入，更新，保存

    # return HttpResponse('OK')
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def delete(request, bid):

    book = BookInfo.objects.get(id=bid)
    book.delete() # 删除
    # return HttpResponseRedirect('/index')
    return redirect('/index')

