from django.conf.urls import url
from . import views as user_views

urlpatterns = [
    url(r'^ll/',user_views.aa),
    url(r'^register/',user_views.register,name='register'),
    url(r'^login/', user_views.login, name='login'),
    url(r'^info/', user_views.user_center_info,name='info'),
    url(r'^order/', user_views.user_center_order,name='order'),
    url(r'^site/', user_views.user_center_site,name='site'),

]