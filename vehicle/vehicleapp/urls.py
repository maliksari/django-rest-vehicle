from django.urls import path, include
from django.conf.urls.static import static

app_name = 'vehicleapp'

urlpatterns = [
    path('', include("vehicleapp.api.urls")),
]
