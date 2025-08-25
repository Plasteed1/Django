from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsAdminOrReadOnly, IsMoverOrReadOnly
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API для работы с сотрудниками.
    Поддержка фильтрации, поиска, сортировки и перемещения сотрудников.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['skills', 'experience_years']

    search_fields = ['name', 'skills']

    ordering_fields = ['name', 'experience_years']

    def get_permissions(self):
        """
        Назначение прав доступа в зависимости от действия.
        """
        if self.action == 'move':
            permission_classes = [IsMoverOrReadOnly]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def move(self, request, pk=None):
        """
        Кастомное действие для перемещения сотрудника между столами.
        Передайте в теле запроса JSON: {"table_number": 5}
        """
        employee = self.get_object()
        table_number = request.data.get('table_number')
        if table_number is None:
            return Response({"detail": "Параметр 'table_number' обязателен."}, status=status.HTTP_400_BAD_REQUEST)

        employee.table_numbe
