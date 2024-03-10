from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name = "register"),
    path("login", views.login, name = "login"),
    path("logout", views.logout, name = 'logout'),
    path("deleteaccount", views.deleteAccount, name = "delete account"),
    path("deletemoderator", views.deleteModerator, name = "delete moderator"),
    path("addFavorite", views.add_favourite, name = 'add favourite'),
    path('removeFavorite', views.remove_favourite, name = 'remove favourite')
]