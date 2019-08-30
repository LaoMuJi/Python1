from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^temp_var$', views.temp_var),
    # url(r'^', ''),
]
