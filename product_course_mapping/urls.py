from django.urls import path
from .views import ProductCourseMappingAPIView


urlpatterns = [

    path('', ProductCourseMappingAPIView.as_view()),

]