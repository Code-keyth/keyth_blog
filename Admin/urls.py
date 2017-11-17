from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^blog_list$',views.blog_list),
    url(r'^blog_add$',views.blog_add),
    url(r'^blog_add_c$',views.blog_add_c),
    url(r'^blog_del$',views.blog_del),
    url(r'^blog_shenhe$',views.blog_shenhe),
    url(r'^skill_category$',views.skill_category),
    url(r'^skill_add$',views.skill_add),
    url(r'^skill_del$',views.skill_del),
    url(r'^skill_list$',views.skill_list),
    url(r'^skill_shenhe$',views.skill_shenhe),

]