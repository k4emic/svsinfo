from django.conf.urls import patterns, url
from service import models

# rest framework
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView

class LocationResource(ModelResource):
    model = models.Location
    
class AreaResource(ModelResource):
    model = models.Area
    
def get_standard_patterns(url_prefix, model_resource):

    base_url = r"^{prefix}/$".format(prefix=url_prefix)
    pk_url = r"^{prefix}/(?P<pk>[^/]+)/$".format(prefix=url_prefix)
    
    return patterns('',
        url(base_url, ListOrCreateModelView.as_view(resource=model_resource)),
        url(pk_url, InstanceModelView.as_view(resource=model_resource))
    )

urlpatterns = get_standard_patterns('locations', LocationResource)
urlpatterns += get_standard_patterns('areas', AreaResource)
