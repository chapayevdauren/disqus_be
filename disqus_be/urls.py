"""This module contains url configuration.

Include your API resources and views into urlpatterns
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from disqus_be.core_app.api import CommentResource

comment_resource = CommentResource()

# define our resource urls

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'bproject.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       (r'^api/v1/', include(comment_resource.urls)),
                       )
