__author__ = 'wanglei02'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^games/$', views.GamesView.as_view(), name='games'),
    url(r'^game/(?P<pk>[0-9]+)/$', views.GameView.as_view(), name='game'),
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyView.as_view(), name='company'),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonView.as_view(), name='person'),
    url(r'^platform/(?P<pk>[0-9]+)/$', views.PlatformView.as_view(), name='platform'),
    url(r'^genre/(?P<pk>[0-9]+)/$', views.GenreView.as_view(), name='genre'),
    url(r'^mode/(?P<pk>[0-9]+)/$', views.ModeView.as_view(), name='mode'),
]
