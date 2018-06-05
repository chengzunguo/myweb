from django.conf.urls import url, include

from App import views


urlpatterns = [

    url('^$',views.home,name='name'),
]
