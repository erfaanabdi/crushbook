from django.conf.urls import patterns, include, url
from Main import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Crush.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index),
    url(r'^sent/$',views.sent),
    url(r'^verify/$',views.verify),
    url(r'^admin/', include(admin.site.urls)),
)
