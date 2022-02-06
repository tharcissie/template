from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from core.views import homepage



urlpatterns = [
    path('me/', admin.site.urls),
    path('', homepage, name='homepage'),

]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)