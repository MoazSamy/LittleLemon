from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import index

urlpatterns = [
    path('', index),
    path('api-token-auth/', obtain_auth_token)
]