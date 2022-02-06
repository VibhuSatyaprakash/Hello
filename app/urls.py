from django.urls import path
from .views import showpost
urlpatterns = [
    path('',showpost.as_view(),name="home"),
]