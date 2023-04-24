from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in_view),
    path('reg/', views.reg, name='reg'),
]
