from django.conf.urls import patterns, include, url

from django.contrib import admin

from demo import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<pk>\d+)/$', views.TaskDetail.as_view(), name='detail'),
    url(r'task/add/$', views.task_add, name='task_add'),
    url(r'task/(?P<pk>\d+)/update/$', views.TaskUpdate.as_view(success_url='/'), name='task_update'),
    url(r'task/(?P<pk>\d+)/delete/$', views.TaskDelete.as_view(), name='task_delete'),
    url(r'task/(?P<pk>\d+)/next/$', views.task_next, name='task_next'),
    url(r'task/(?P<pk>\d+)/active/$', views.task_active, name='task_active'),
    url(r'', 'demo.views.default_page', name='list'),
)
