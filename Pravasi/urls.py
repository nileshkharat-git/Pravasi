from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
import main.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('user/',include(main.urls)),
    path('explore/',views.explorer,name='explorer'),

]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
