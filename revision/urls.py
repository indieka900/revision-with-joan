from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

#pip install Pillow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('revision_app.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
