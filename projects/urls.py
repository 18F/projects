from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^client-autocomplete/$', views.ClientAutocomplete.as_view(),
        name='client-autocomplete'),
]
