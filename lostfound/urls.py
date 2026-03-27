from django.contrib import admin
from django.urls import path , include
from items import views as item_views
from accounts import views as acc_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item_views.home, name='home'),
     path('', include('accounts.urls')),
    path('', include('items.urls')), 
    path('chat/', include('chat.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)