from django.urls import path
from. import views

app_name = 'movieapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),  # homepage
    path('search/', views.SearchView.as_view(), name='search'),
    path('search_result/', views.SearchResultView.as_view(), name='search_result'),

    path("country_list/", views.CountryListView.as_view(), name="country_list"),
    path("country_detail/<int:pk>", views.CountryDetailView.as_view(), name="country_detail"),

    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),  # Movie List View
    path('movie_detail/<int:pk>', views.MovieDetailView.as_view(), name='movie_detail'),  # Movie detail View


]

