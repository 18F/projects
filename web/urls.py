from django.conf.urls import url

from web.views.home import HomeView
from web.views.logout import LogoutView
from web.views.project import ProjectView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^p/(?P<pk>[\w/\-]+)?$', ProjectView.as_view(), name='project'),
]
