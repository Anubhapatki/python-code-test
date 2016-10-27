from django.conf.urls import url
from .views import StarshipAPIListView

urlpatterns = [
    url("", StarshipAPIListView.as_view(), name="sharship_list")
]