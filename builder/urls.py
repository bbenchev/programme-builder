from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('modules/', views.get_modules, name="modules"),
    path('modules/<int:id>/', views.module),
    path('build/', views.build, name="build"),
]