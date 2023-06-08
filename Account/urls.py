from django.urls import path, url
from . import views
app_name = 'accounts'
urlpatterns = [
    path("contact/", views.contact, name="contact"),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    # path('login/', views.login_view, name='login'),
    # path('register/', views.register_view, name='register'),

]