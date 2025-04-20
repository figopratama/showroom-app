from django.contrib import admin
from django.urls import path, include
from core.views import index, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('cars/', include('cars.urls')),
]
