from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tpt_server.views.home', name='home'),
    # url(r'^tpt_server/', include('tpt_server.foo.urls')),
    url(r"^$", TemplateView.as_view(template_name="index.html")),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
