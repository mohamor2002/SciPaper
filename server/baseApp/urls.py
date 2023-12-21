from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deletemoderator", views.deleteModerator, name = "delete moderator")

]