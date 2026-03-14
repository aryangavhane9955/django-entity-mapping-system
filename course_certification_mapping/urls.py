from django.urls import path
from .views import CourseCertificationMappingAPIView


urlpatterns = [

    path('', CourseCertificationMappingAPIView.as_view()),

]