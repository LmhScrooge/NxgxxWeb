from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
    #url(r'^$',views.news,name='news'),
    url(r'^$', views.home, name='homeindex'),
]