from django.conf.urls import url
from .views import StarshipAPIListView, StarshipClassListView, StarshipListing

urlpatterns = [
    url("starships/", StarshipAPIListView.as_view(), name="sharship_list"),
    url("starships/<str:starship_class>", StarshipClassListView.as_view(), name="sharship_list"),
    url("listing/", StarshipListing.as_view(), name="sharship_listing")

]