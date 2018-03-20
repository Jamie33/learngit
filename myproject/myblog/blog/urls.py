
from django.conf.urls import url

from . import views # . 代指当前包，包内导入
#from blog import views


app_name = 'blog'
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name='edit_page'),
    url(r'^edit/action/$',views.edit_action,name='edit_action'),
]