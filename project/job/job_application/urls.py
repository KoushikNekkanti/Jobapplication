from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("dash/", views.dasha, name="dasha"),
    path("dashboard/", views.dashb, name="dashb"),
]