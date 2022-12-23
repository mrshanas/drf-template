from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Starter API',
        default_version='v1',
        description='Starter Backend API',
        contact=openapi.Contact(email='nassibshaban345@gmail.com'),
        license=openapi.License(name='MIT')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/',include('users.urls')),

     # docs
    path('', schema_view.with_ui(
        'swagger',
        cache_timeout=0
    ),
        name='Schema-Swagger-UI'
    ),
    path('schema',schema_view.without_ui())
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
