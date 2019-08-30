from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def set_session(resquest):
    resquest.session['username'] = 'liu'
    resquest.session['age'] = 18

    return HttpResponse('设置session')

def get_session(resquest):
    username = resquest.session['username']
    age = resquest.session['age']

    return HttpResponse(username+str(age))