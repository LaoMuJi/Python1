from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import BookInfo
# Create your views here.

def temp_var(request):
    my_dict = {'title':'字典123'}
    my_list = [1,2,3]
    book = BookInfo.objects.get(id=105)

    context = {'my_dict':my_dict,'my_list':my_list,'book':book}
    return render(request,'boottest/temp_var.html', context)