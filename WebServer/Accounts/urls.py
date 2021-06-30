from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_page, name='Login'),
    path('logout/', views.logout_page, name='Logout'),

]