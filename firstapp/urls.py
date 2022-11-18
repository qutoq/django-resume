from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import pnf


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', views.main, name='main'),
    path('res/', views.res, name='res'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]

handler404 = pnf

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)