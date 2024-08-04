from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data_analysis.urls')),  # Include the URLs from the data_analysis app
]