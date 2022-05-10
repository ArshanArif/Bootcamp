from django.urls import path
from . import views


urlpatterns = [
    path('signup',views.page, name='page'),
    path('login',views.loginpage, name='loginpage'),
    path('',views.bstrap, name='bstrap'),
    path('courses',views.secpage, name='secpage'),

]