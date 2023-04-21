from django.urls import path
from . import views


urlpatterns = [
    path("<pk>/",views.create_book,name="create_book"),
    path("",views.index,name="index"),
    path("htmx/book_form/",views.create_book_form,name="book_form"),
    path("htmx/book/<pk>/",views.detail_book,name="detail_book"),
    path("htmx/book/<pk>/delete/",views.delete_book,name="delete_book"),
    path("html/book/<pk>/update/",views.update_book,name="update_book")


]