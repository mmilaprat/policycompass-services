from django.conf.urls import patterns, url
from apps.eventsmanager import views
from .views import *

urlpatterns = patterns('',
     #url(r'^', include(router.urls)),
     url(r'^events$', views.EventView.as_view(), name='author-list'),
     url(r'^events/(?P<pk>[\d]+)$', views.EventInstanceView.as_view(), name='event-instance'),
     url(r'^harvestevents$', views.HarvestEvents.as_view(), name='harvest-events'),
     url(r'^configextractor$', views.ConfigExtractor.as_view(), name='config-extractor'),
     url(r'^configupload$', views.ConfigUpload.as_view(), name='config-upload'),
     url(r'^', Base.as_view(), name="event-base")
)