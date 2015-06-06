from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',


	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'polls.views.index'),
    url(r'^poll/$', 'polls.views.poll'),
    url(r'^choice/(\d+)/', 'polls.views.choice'),
    url(r'^write/$','polls.views.write'),
    url(r'^write/new/$','polls.views.write_new'),
    url(r'^test/$','polls.views.test'),
    url(r'^test/write/$','polls.views.test_write'),
    url(r'^mobile/$', 'polls.views.test_mobile'),
        


    url(r'^buddy/$', 'buddy.views.index'),    
    url(r'^buddy/intro/$', 'buddy.views.intro'),    
    url(r'^buddy/procedure/$', 'buddy.views.procedure'),    
    url(r'^around/$', 'buddy.views.around'),    
    url(r'^signup/$', 'buddy.views.signup'),
    url(r'^detail/$', 'buddy.views.detail'),
    url(r'^createdetail/$', 'buddy.views.createdetail'),
    url(r'^login/$', 'buddy.views.login'),
    url(r'^logout/$', 'buddy.views.logout'),
    url(r'^create/$', 'buddy.views.create'),
    url(r'^authenticate/$', 'buddy.views.authenticate'),

    url(r'^aim/$', 'buddy.views.aim'),    
    url(r'^aimq/$', 'buddy.views.aimq'),    
    url(r'^recommend/$', 'buddy.views.recommend'),    

    url(r'^youtravel/$', 'buddy.views.youtravel'),    
    
    url(r'^zip/$', 'zip.views.index'),    
    url(r'^zip/up$', 'zip.views.up'),    
    url(r'^zip/upload$', 'zip.views.upload'),    
     
    url(r'^about/$', 'buddy.views.about'),    
    url(r'^python/$', 'buddy.views.python'),    
    url(r'^python/1/$', 'buddy.views.python1'),    

    url(r'^my/','sowe.views.my'),
    url(r'^you/','sowe.views.you'),
    url(r'^(\d+)/$','sowe.views.each'),  
    url(r'^register/','sowe.views.register'),
	)
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
