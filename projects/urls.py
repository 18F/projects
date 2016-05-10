from django.conf.urls import url

from projects.views.home import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
