from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import datetime

'''
render          返回一个页面
redirect        跳转某个地址
HttpResponse    直接返回变量
JsonResponse    返回json
'''


def index(request):
    return render(request, 'booktest/index.html')


def show_arg(request,num):
    return HttpResponse(num)


def login(request):
    if request.session.has_key('YES'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES: # 判断cookie里面username存在
            username = request.COOKIES['username'] # 获取用户名
        else:
            username = ''
        return render(request, 'booktest/login.html', {'username':username})


def login_check(request):
    '''
    request.POST    request.GET
    传过来的类似字典，允许一个名字对应多个值
    '''
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    # print(request.path) # 显示请求的完整路径，不包含域名
    # print(request.method) # 显示HTTP请求方法，get，post

    if username == '0' and password == '0':
        respones = redirect('/index')
        if remember == 'on': # 判断是否记住用户名
            respones.set_cookie('username', username, max_age=7*24*3600) # 设置cookie
        request.session['YES'] = True
        return respones
    else:
        return redirect('/login')


def ajax_test(request):
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(requset):
    return JsonResponse({'res':1})


def login_ajax(request):
    return render(request,'booktest/login_ajax.html')



def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == '0' and password == '0':
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})


def set_cookie(request):
    response = HttpResponse('已设置cookie')
    # response.set_cookie('num', 1, max_age=14*24*3600)
    response.set_cookie('num', 'aDFssCHWEdfsgdfgvhbdfkgd', expires=datetime.datetime.now()+datetime.timedelta(days=14))
    return response

def get_cookie(request):
    num = request.COOKIES['num']
    return HttpResponse(num)



def set_session(request):
    request.session['username'] = '我的名字'
    request.session['age'] = 18
    request.session.set_expiry(7) # 秒数，0是浏览器关闭删除，不写是两周
    return HttpResponse('设置session')

def get_session(request):
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+str(age))

def clear_session(request):
    # request.session.clear() # 清除session，只清值，不完全清除
    request.session.flush() # 完全清除session
    return HttpResponse('清除session')
