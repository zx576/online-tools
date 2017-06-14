from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    # 工具
    url('^qrcode/$', views.qrcode, name='qrcode'),
    url('^base64/$', views.base64, name='base64'),
    url('^conv/$', views.convertion, name='conv')

]