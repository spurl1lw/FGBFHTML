from django.conf.urls import patterns, include, url
from fiveguys import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^Login/', 'checklist.views.fg_login',name='Login'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^Build_Checklist/', 'checklist.views.manager_home',name='manager_home'),
     url(r'^admin_home/', 'checklist.views.admin_home',name='admin_home'),
     url(r'^report/', 'checklist.views.report',name='report'),
     url(r'^new_location/', 'checklist.views.new_location',name='new_location'),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^Create_Template/', 'checklist.views.CreateTemplate',name='Create_Template'),
     url(r'^Users/', 'checklist.views.Users',name='Users'),
     url(r'^Email_Settings/', 'checklist.views.email_settings',name='Settings'),
      url(r'^Checklist/', 'checklist.views.fill_checklist',name='Fill_Checklist'),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)