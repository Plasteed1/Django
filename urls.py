from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view=get_schema_view(
   openapi.Info(
      title="Group Funds API",
      default_version='v1'
   ),
   public=True,
)
urlpatterns=[
   path('api/', include('core.urls')),
   path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger'),
]
