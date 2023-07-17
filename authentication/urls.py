from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('', views.dash, name='dash'),
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('log', views.log, name='log'),
    # other URL patterns
]
