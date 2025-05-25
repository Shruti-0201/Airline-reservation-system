from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_form, name='search_form'),  # shows the form (flights.html)
    path('results/', views.search_results, name='search_results'),  # processes and shows results.html
    path('popular-routes/', views.popular_routes, name='popular_routes'),# shows the form (flights.html)
    path('airport/', views.airport_info_view, name='airport_info'),# shows the form (airport_info.html)
    path('travel/', views.travel, name='travel_tip'),# shows the form (travel_tip.html)
]
