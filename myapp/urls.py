from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from myapp import views



urlpatterns = [
    path('', views.home, name='root_home'),
    path('home/', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('search/', views.search_form, name='search_form'),
    path('results/', views.search_results, name='search_results'),
    path('popular-routes/', views.popular_routes, name='popular_routes'),
    path('airport/', views.airport_info_view, name='airport_info'),
    path('travel/', views.travel, name='travel_tip'),
]
