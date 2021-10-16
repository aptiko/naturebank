from django.conf.urls import url
from django.conf import settings
from django.views.generic.base import RedirectView

from naturebank import views
from naturebank.models import Biotope, Species

biotope_list = {
    "queryset": Biotope.objects.all(),
    "allow_empty": True,
    "extra_context": {},
}

species_list = {
    "queryset": Species.objects.all(),
    "allow_empty": True,
    "extra_context": {},
}

urlpatterns = [
    url(r"^biotopes/$", views.BiotopeListView.as_view(), name="biotope_list"),
    url(
        r"^biotopes/d/(?P<pk>\d+)/$",
        views.BiotopeDetailView.as_view(),
        name="biotope_detail",
    ),
    url(
        r"^biotopes/c/(?P<site_code>[^/]+)/$",
        views.BiotopeDetailView.as_view(),
        name="biotope_detail",
    ),
    url(
        r"^biotopes/b/(?P<pk>\d+)/$",
        views.BiotopeDetailBriefView.as_view(),
        name="biotope_brief",
    ),
    url(r"^biotope_list_filter/(?P<filter_name>[^/]+)/$", views.biotope_list_filter),
    url(r"^species/$", views.SpeciesListView.as_view(), name="species_list"),
    url(
        r"^species/d/(?P<pk>\d+)/$",
        views.SpeciesDetailView.as_view(),
        name="species_detail",
    ),
    url(r"^(?P<layer>[^/]+)/kml/$", views.kml, {}),
    url(r"^bound/$", views.bound, {}),
    url(r"^settlements/$", views.settlements_kml, {}),
]
