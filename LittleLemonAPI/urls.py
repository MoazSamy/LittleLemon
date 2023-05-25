from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "LittleLemonAPI"
urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name="menu-items"),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]