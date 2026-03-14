from django.urls import path
from .views import VendorProductMappingAPIView


urlpatterns = [

path('', VendorProductMappingAPIView.as_view()),

]