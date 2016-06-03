from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('web.urls', namespace='web')),
    url(r'^', include('projects.urls', namespace='projects')),
    url(r'^admin/', admin.site.urls),
]
