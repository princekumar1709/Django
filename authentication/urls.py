from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash, name='dash'),
    path('signup', views.signup, name='signup'),
    path('log', views.log, name='log'),
    path('logout', views.logout, name='logout'),
    path('upload', views.upload, name='upload'),
    path('visual', views.visual, name='visual'),
]
