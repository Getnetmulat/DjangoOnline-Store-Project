from django.urls import path
from .views import greet_new_user
from .views import user_profile
from .views import user_profile_enhanced
urlpatterns = [

path('greet/', greet_new_user, name='greet_new_user'),
path('staff/', user_profile, name='staff'),
path('profile/enhanced/', user_profile_enhanced, name='user_profile_enhanced'),
    

]