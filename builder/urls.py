from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login_handler, name="index"),
    path('home/', views.home, name="home"),
    path('signup/', views.signup_handler, name="signup"),
    path('logout/', views.logout_handler, name="logout"),
    path('modules/', views.get_modules, name="modules"),
    path('modules/<int:id>/', views.module),
    path('build/', views.build, name="build"),
    path('ajax/check_fulfilled/<int:id>/', views.check_fulfilled)
]