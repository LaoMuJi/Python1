from django.shortcuts import render
from django.http import HttpResponse

from .models import BookInfo

from django.template import loader, RequestContext


# Create your views here.



# 1.定义视图函数，HttpRequest
# 2.进行url配置，建立url地址和视图的关系



# 127.0.0.1:8000/index
# def index(request):
#
#     # 加载模板文件
#     temp = loader.get_template('booktest/index.html')
#
#     # 给模板传递数据
#     context = RequestContext(request, {})
#
#     # 产生标准的html内容
#     res_html = temp.render(context)
#
#     return HttpResponse(res_html)



def my_render(request, temeplate_path, context_path={}):

    temp = loader.get_template(temeplate_path)

    context = RequestContext(request, context_path)

    res_html = temp.render(context)

    return HttpResponse(res_html)


def index(request):
    return render(request, 'booktest/index.html', {'content': '变量A', 'list': list(range(1,10))})



def show_book(request):

    books = BookInfo.objects.all()

    return render(request, 'booktest/show_books.html', {'book': books})

