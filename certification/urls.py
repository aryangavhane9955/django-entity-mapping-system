from django.urls import path
from .views import CertificationListCreate


urlpatterns = [

    path('', CertificationListCreate.as_view()),

]