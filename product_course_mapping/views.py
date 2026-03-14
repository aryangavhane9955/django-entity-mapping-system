from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer


class ProductCourseMappingAPIView(APIView):

    def get(self, request):
        mappings = ProductCourseMapping.objects.all()
        serializer = ProductCourseMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)