from django.conf.urls import patterns, include, url
from django.contrib import admin

import send_message.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_li.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'send_message.views.send_message', name='send_message'),
    url(r'^admin/', include(admin.site.urls)),
)
