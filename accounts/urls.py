from django.urls import path, include
from accounts import views

urlpatterns = [
    path('inscription/', views.signup, name='signup'),
    path('connexion', views.login_user, name='login_user'),
    path('deconnexion', views.logout_user, name='logout_user'),

]
