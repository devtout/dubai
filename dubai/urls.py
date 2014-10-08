from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'dubai_.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contato/','contato.views.contato'),
    url(r'^cadastro/','usuario.views.cadastro'),
    url(r'^login/','usuario.views.login_view'),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

