from django.conf.urls import url
from . import views

app_name = 'report'
urlpatterns = [
    url(r'login', views.login, name='login'),
    #url(r'report/list', views.list, name='report_list'),
]
