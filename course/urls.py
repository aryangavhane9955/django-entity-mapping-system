from django.urls import path
from .views import CourseListCreate

urlpatterns = [
    path('', CourseListCreate.as_view()),
]