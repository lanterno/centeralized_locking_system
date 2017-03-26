from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^request/(?P<pk>\d+)/$', views.RequestResourceApiView.as_view()),
    url(r'^release/(?P<pk>\d+)/$', views.ReleaseResourceApiView.as_view()),
]
