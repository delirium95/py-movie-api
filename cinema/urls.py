from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
   path("", movie_list, name="movie-list"),
   path("", movie_detail, name="movie-detail")
]

app_name = "cinema"
