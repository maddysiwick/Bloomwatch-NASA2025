from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("superbloom2022/", views.superbloom2022, name="superbloom2022"),
    path("superbloom2023/", views.superbloom2023, name="superbloom2023"),
    path("process-slider2023/", views.process_slider2023, name="process_slider2023"),
    path("process-slider2022/", views.process_slider2022, name="process_slider2022"),
]