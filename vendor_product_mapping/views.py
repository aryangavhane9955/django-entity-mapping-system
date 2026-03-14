from rest_framework.views import APIView
from rest_framework.response import Response

from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer


class VendorProductMappingAPIView(APIView):

    def get(self, request):

        mappings = VendorProductMapping.objects.all()
        serializer = VendorProductMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = VendorProductMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)