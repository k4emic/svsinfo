from django.conf.urls import patterns, url
import views

urlpatterns = patterns('webclient.views',
    url('', views.index)
)
