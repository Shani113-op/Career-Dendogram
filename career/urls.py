from django.contrib import admin
from django.urls import path
from career import views

urlpatterns = [
    path("",views.index, name="index"),
    path("login",views.loginuser, name="login"),
    path("register",views.register, name="register"),
    path("logout",views.logoutUser, name="logout"), 
    path("home",views.home, name="home"),
    path("profile",views.profile, name="profile"),
    path("explore",views.explore, name="explore_career"),
    path("success",views.success, name="success_story"),
    path("career", views.career, name="career_option"),
    path("goals", views.goal, name="setgoals"),
    path("tests", views.test, name="tests")
]
