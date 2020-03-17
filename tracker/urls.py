from django.urls import path
from . import views


app_name = "tracker"
urlpatterns = [
    path('', views.Cases.as_view(), name="index"),
]
