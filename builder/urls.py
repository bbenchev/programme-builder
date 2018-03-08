from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modules/', views.get_modules),
    path('modules/<int:id>/', views.module)
]