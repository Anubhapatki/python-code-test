from django.conf.urls import url
from .views import StarshipAPIListView, StarshipClassListView,  StarshipListingDetail,StarshipListing

urlpatterns = [
    url(r'^starships/', StarshipAPIListView.as_view(), name="sharship_list"),
    url(r'^starships_per_class/(?P<starship_class>[\w]+)$', StarshipClassListView.as_view()),
    url(r'^listings/', StarshipListing.as_view(), name="sharship_listing"),
    url(r'^listing/(?P<id>\d+)$', StarshipListingDetail.as_view())

]