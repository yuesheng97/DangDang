from  django.conf.urls import url
from . import views



urlpatterns=[
    url(r'^main/$',views.Main),
    url(r'^base/$',views.base),
    url(r'^getmodel/$',views.getmodel),
    url(r'^phone/(\w+)/(\d+)$',views.selectModel),
    url(r'^detail/$',views.detail),
    url(r'^getdetail/',views.getdetail),
    url(r'^signin/$',views.signin)
]