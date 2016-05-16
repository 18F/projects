from django.conf.urls import include, url

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'projects', views.ProjectsViewSet, base_name='projects')

urlpatterns = [
    url(r'^', include(router.urls))
]
