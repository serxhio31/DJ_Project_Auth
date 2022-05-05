from django.urls import path
from . import views


urlpatterns = [
    path('index',views.index, name = 'index'),
    path('counter',views.counter, name = 'counter'),
    path('home',views.static, name = 'home'),
    path('register', views.register , name = 'register'),
    path('login', views.login , name='login'),
    path('logout', views.logout , name='logout')
]