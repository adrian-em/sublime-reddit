from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sublimereddit.apps.sublime.views.main_page', name='home'),
    url(r'^subreddit/(?P<subreddituri>[\w|\W]+)/$', 'sublimereddit.apps.sublime.views.subreddit_page', name="subreddit"),
    url(r'^page/(?P<after>[\w|\W]+)/$', 'sublimereddit.apps.sublime.views.reddit_next_page', name="nextpage"),
    url(r'^comments/(?P<r>[\w|\W]+)/(?P<subreddit>[\w|\W]+)/(?P<comments>[\w|\W]+)/(?P<name>[\w|\W]+)/(?P<title>[\w|\W]+)/$',
    'sublimereddit.apps.sublime.views.comments_page', name="comments"),
    url(r'^settings/$', 'sublimereddit.apps.sublime.views.settings_page', name="settings"),
    (r'^robots\.txt$', direct_to_template,
     {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    # url(r'^sublimereddit/', include('sublimereddit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
