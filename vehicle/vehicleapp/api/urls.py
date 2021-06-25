from django.urls import path
from django.conf.urls.static import static
from .views import *
app_name = 'vehicle-api'

urlpatterns = [
    path('vehicle-model', VehicleModelView.as_view(), name='vehicle-model'),
    path('vehicle-model-detail/<int:pk>',
         VehicleModelDetail.as_view(), name="vehicle-model-detail"),
    # Vehicle path
    path('vehicle', VehicleView.as_view(), name='vehicle'),
    path('vehicle-detail/<int:pk>', VehicleDetail.as_view(), name='vehicle-detail'),
    #path('test', testClass.as_view() , name='test'),

]
