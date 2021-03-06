from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from core.api.views import PatientViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    url(r'^submit$', 'core.views.submit', name='submit'),
    
    url(r'^query$', 'core.views.query', name='query'),

    
    url(r'^admin/', include(admin.site.urls)),

    # API Routes
    url(r'^api/', include(router.urls)),

    # API Auth Urls
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
)
