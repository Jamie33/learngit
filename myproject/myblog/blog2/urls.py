from django.conf.urls import url

from . import views # . 代指当前包，包内导入
#from blog import views

urlpatterns = [
    url(r'^home/$', views.index),
]