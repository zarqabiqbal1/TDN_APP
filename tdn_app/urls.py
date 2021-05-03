from django.urls import path,re_path
from tdn_app import views


urlpatterns = [
    path('create_user', views.UserView.as_view(),name = 'user_create'),
]