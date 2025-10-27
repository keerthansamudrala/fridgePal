from django.urls import path
from . import views

urlpatterns = [
    # URL for the homepage
    path('', views.homepage, name='homepage'),

    # URL for the signup page
    path('signup/', views.signup_view, name='signup'),

    # URL for the login page
    path('login/', views.login_view, name='login'),

    # URL for the logout functionality
    path('logout/', views.logout_view, name='logout'),

    # URL for the pantry page (the destination after a successful login)
    path('pantry/', views.pantry_view, name='pantry'),
]

