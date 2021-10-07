from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]


urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.index, name="index"),
]