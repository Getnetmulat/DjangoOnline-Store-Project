from django.urls import path, url
from . import views

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
]