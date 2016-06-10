from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('web.urls', namespace='web')),
    url('^auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
