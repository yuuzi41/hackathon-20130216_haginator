from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testprj.views.home', name='home'),
    # url(r'^testprj/', include('testprj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'hogehoge/$', 'hogehoge.views.index'),
    (r'hogehoge/result$', 'hogehoge.views.result'), 
    (r'hogehoge/matrix$', 'hogehoge.views.matrix'), 
    (r'hogehoge/edit$', 'hogehoge.views.edit'),
    (r'hogehoge/prob/import$', 'hogehoge.views.prob_import'),
    (r'hogehoge/prob/learn$', 'hogehoge.views.prob_learn'),
    (r'hogehoge/prob/new$', 'hogehoge.views.prob_new'),
    (r'hogehoge/prob/result$', 'hogehoge.views.prob_result'),
)
