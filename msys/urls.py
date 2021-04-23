from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from msys.views import Entercc1
from msys.views import Entercc2
from msys.views import Enteracl

urlpatterns = [

path('',views.Select.as_view(), name='select'),
path('page1',views.Page1.as_view(), name='page1'),
#url('login', auth_views.login, name='login'),
path('logincc1.html',views.Logincc1.as_view(), name='logincc1'),
path('logincc2.html',views.Logincc2.as_view(), name='logincc2'),
path('loginacl.html',views.Loginacl.as_view(), name='loginacl'),
path('choosecc1.html',views.Choosecc1.as_view(), name='choosecc1'),
path('choosecc2.html',views.Choosecc2.as_view(), name='choosecc2'),
path('chooseacl.html',views.Chooseacl.as_view(), name='chooseacl'),
path(r'entercc1.html', Entercc1.as_view(), name= 'DataEntrycc1'),
path(r'entercc2.html', Entercc2.as_view(), name= 'DataEntrycc2'),
path(r'enteracl.html', Enteracl.as_view(), name= 'DataEntrycc3'),
path(r'successcc1/<int:pk>',views.Successcc1.as_view(), name='successcc1'),
path(r'successcc2/<int:pk>',views.Successcc2.as_view(), name='successcc2'),
path(r'successacl/<int:pk>',views.Successacl.as_view(), name='successacl'),
#url(r'^login/$', auth_views.login, {'template_name': 'msys/logincc1.html'}, name='logincc1'),


]