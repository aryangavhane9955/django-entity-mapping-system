from django.urls import path
from .views import VendorListCreate, VendorDetail


urlpatterns = [

path('', VendorListCreate.as_view()),
path('<int:pk>/', VendorDetail.as_view()),

]