from django.conf.urls import patterns, include, url  
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
# Examples:
        # url(r'^$', 'myDj.views.home', name='home'),
	    # url(r'^blog/', include('blog.urls')),
		url(r'^gpss/post/$','gpss.views.test'),
		url(r'^gpss/post/test/$','gpss.views.post'),
	        url(r'^admin/', include(admin.site.urls)), 
		)
'''
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
	            'document_root': settings.STATIC_ROOT,
		        }),
			)
'''
