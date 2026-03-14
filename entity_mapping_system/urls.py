from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Entity Mapping API",
        default_version='v1',
        description="Vendor Product Course Certification System",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/vendor/', include('vendor.urls')),
    path('api/product/', include('product.urls')),
    path('api/course/', include('course.urls')),
    path('api/certification/', include('certification.urls')),

    path('api/vendor-product/', include('vendor_product_mapping.urls')),
    path('api/product-course/', include('product_course_mapping.urls')),
    path('api/course-certification/', include('course_certification_mapping.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),

]