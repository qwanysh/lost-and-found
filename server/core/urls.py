from django.contrib import admin
from django.urls import path, include

api_urlpatterns = [
    path('lost-items/', include('lost_items.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]
