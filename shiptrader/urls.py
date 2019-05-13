from django.conf.urls import url
from .views import StarshipAPIListView, StarshipClassListView, StarshipListing, UpdateStarshipListing

urlpatterns = [
    url("starships/", StarshipAPIListView.as_view(), name="sharship_list"),
    url("starships/<str:starship_class>", StarshipClassListView.as_view(), name="sharship_list"),
    url("listing/", StarshipListing.as_view(), name="sharship_listing"),
    url("listing/(?P<id>\d+)$", UpdateStarshipListing.as_view())

]