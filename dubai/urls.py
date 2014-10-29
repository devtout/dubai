from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'dubai_.views.index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^contact/','contato.views.contact'),
                       url(r'^register/','usuario.views.register'),
                       url(r'^login/','usuario.views.login_view'),
                       url(r'^logout/','usuario.views.logout_view'),
                       url(r'^news/(?P<slug>[\w_-]+)/$', 'imprensa.views.news_detail'),
                       url(r'^occurrence/', 'contato.views.occurrence'),
                       url(r'^gallery/', 'imprensa.views.gallery'),
                       url(r'^file/', 'imprensa.views.album'),
                       url(r'^download/', 'imprensa.views.download'),
                       )+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

