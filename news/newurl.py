from django.conf.urls import url
from . import views

app_name = 'news'
urlpatterns = [
    #url(r'^$',views.news,name='news'),
    #url(r'^index$', views.index, name='index'),
    url(r'^articles/(?P<Article_id>[0-9]+)',views.detail,name='detail'),
    url(r'^index/(?P<Page_num>[0-9]+)',views.newspage,name='page'),
]