from django.urls import path
from . import views
from sign_in.views import sign_in_view

urlpatterns = [
    path('', views.index),
    path('sign_in/', sign_in_view, name='sign_in'),
]
