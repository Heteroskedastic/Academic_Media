from django.urls import path, include
from . import (views, router)

app_name = "app"


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),    # Home Page
    path('accounts/login/', views.LoginView.as_view(), name='login'),    # Login Page
    path('accounts/signup', views.SignUp.as_view(), name='signup'),    # SignUP Page

]
urlpatterns += router.router.urls