
from django.conf.urls import url,include
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^myapp/', include('myapp.urls')),
    url(r'^$',views.Main),
    #下方为支付宝添加的
    url(r'^page1/', views.page1),
    url(r'^page2/', views.page2),
    
]
