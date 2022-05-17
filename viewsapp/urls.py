from django.urls import path
from viewsapp.views import HomeView

homeApiView = [
    path('',HomeView.as_view(),name='home')
];