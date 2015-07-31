"""gamemob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from gamemob import views

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^', include('main.urls', namespace='main')),
                  url('^', include('django.contrib.auth.urls')),
                  url(r'^register/$', CreateView.as_view(template_name='registration/register.html',
                                                         form_class=UserCreationForm,
                                                         success_url=reverse_lazy('register_succeed')),
                      name='register'),
                  url(r'^register_succeed/$', views.register_succeed, name='register_succeed'),
                  url(r'^polls/', include('polls.urls', namespace='polls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
