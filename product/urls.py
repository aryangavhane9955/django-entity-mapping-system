from django.urls import path
from .views import ProductListCreate, ProductDetail


urlpatterns = [

path('', ProductListCreate.as_view()),
path('<int:pk>/', ProductDetail.as_view()),

]