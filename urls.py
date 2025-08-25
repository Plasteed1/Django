from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/token/', include('rest_framework_simplejwt.views.TokenObtainPairView')),
    path('api/token/refresh/', include('rest_framework_simplejwt.views.TokenRefreshView')),
]
