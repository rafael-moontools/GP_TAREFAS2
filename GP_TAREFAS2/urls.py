from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('core.views',
    url(r'^$', 'home', name='home'),

    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),

    url(r'^tarefas/$', 'tarefas', name='tarefas'),
    url(r'^file_upload/$', 'file_upload', name='file_upload'),

    url(r'^smart_admin/$', 'smart_admin', name='smart_admin'),


    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
)
