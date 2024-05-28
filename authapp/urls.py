from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('counter',views.counter,name="counter"),
    path('workout',views.workout,name="workout"),
    path('calculate_calories', views.calculate_calories, name='calculate_calories'),
]
