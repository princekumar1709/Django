from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('', views.dash, name='dash'),
    path('login/', views.login_view, name='login'),
    path('login/register/', views.register, name='register'),
    # other URL patterns
]
