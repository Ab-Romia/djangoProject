from django.urls import path
from . import views

urlpatterns = {
    path('', views.form_view, name="form"),
    path('book/', views.book, name="book"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
    path('login/', views.login, name="login"),
}
