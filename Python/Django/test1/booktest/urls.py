from django.conf.urls import url
from . import views

urlpatterns = [
    # 通过url函数设置url路由配置
    url(r'^index$', views.index),
    url(r'^books', views.show_book), #现实图书信息
]

