from django.conf.urls import patterns, url
from service.model_resources import LocationResource, AreaResource, EventResource, ActivityResource, NewsItemResource

# rest framework
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
    
def get_standard_patterns(url_prefix, model_resource):

    base_url = r"^{prefix}/$".format(prefix=url_prefix)
    pk_url = r"^{prefix}/(?P<pk>[^/]+)/$".format(prefix=url_prefix)
    
    return patterns('',
        url(base_url, ListOrCreateModelView.as_view(resource=model_resource)),
        url(pk_url, InstanceModelView.as_view(resource=model_resource))
    )

urlpatterns = get_standard_patterns('locations', LocationResource)
urlpatterns += get_standard_patterns('areas', AreaResource)
urlpatterns += get_standard_patterns('events', EventResource)
urlpatterns += get_standard_patterns('activities', ActivityResource)
urlpatterns += get_standard_patterns('news', NewsItemResource)