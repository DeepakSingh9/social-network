from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^post/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',views.post_detail,name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$',views.post_new,name='post_new'),
    url(r'^profile/(?P<pk>\d+)/$',views.profile,name='profile'),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[\w-]+)/edit/$', views.post_edit, name='post_edit'),


]