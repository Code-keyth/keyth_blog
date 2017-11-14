from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^blog_list',views.blog_list),
    url(r'^blog_add',views.blog_add),
    url(r'^skill_category',views.skill_category),
    url(r'^skill_list',views.skill_list),
    url(r'^skill_lis111',views.skill_lis111),
    url(r'^welcome',views.welcome),
]