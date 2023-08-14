from django.urls import path
from . import views

app_name="polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:questionId>/", views.detail, name="detail"),
    path("<str:questionId>/vote/", views.vote, name="vote"),
    path("<str:questionId>/results/", views.results, name="results"),
]
