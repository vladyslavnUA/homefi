from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('detail/', detail, name='detail'),
    path('<int:id>/', single, name='single'),
    path('new-listing/', new_listing, name='new_listing'),
    path('edit-listing/<int:id>/', edit_listing, name='edit_listing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)