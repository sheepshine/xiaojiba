from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail/(?P<article_id>[0-9]+)$', views.detail, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit, name='edit'),
    url(r'^edit/action$', views.edit_action, name='edit_action')
]