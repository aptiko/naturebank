from django.contrib.gis import admin
from django.conf import settings
from django.conf.urls import include, patterns
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'', include('naturebank.urls')),
    (r'', include('django.contrib.flatpages.urls')),
)

if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT) + urlpatterns
