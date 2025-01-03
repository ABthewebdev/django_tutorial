from django.urls import path
from . import views


urlpatterns = [
    path("create/", views.create, name='create'),
    path("<str:name>/", views.index, name='index'),
    path('', views.home, name='home')
]