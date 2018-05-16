from django.conf.urls import url
from . import views as goods_views

urlpatterns = [
    url(r'^cart/', goods_views.cart,name='cart'),
    url(r'^detail/', goods_views.detail,name='detail'),
    url(r'^index/', goods_views.index,name='index'),
    url(r'^list/', goods_views.list,name='list'),
    # url(r'^index/', goods_views.index),

]