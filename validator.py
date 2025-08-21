from django.core.exceptions import ValidationError
from .models import Employee
def validate_desk_neighbors(instance):
    if not hasattr(instance, 'desk_number') or instance.desk_number is None:
        return

    neighbor_desks = [instance.desk_number - 1, instance.desk_number + 1]

    for neighbor_desk in neighbor_desks:
        neighbors = Employee.objects.filter(desk_number=neighbor_desk)
        for neighbor in neighbors:
            position_lower_self = instance.position.lower()
            position_lower_neighbor = neighbor.position.lower()
            if ('тестировщик' in position_lower_self and (
                'бекенд' in position_lower_neighbor or 'фронтендер' in position_lower_neighbor)) or \
                ('тестировщик' in position_lower_neighbor and (
                    'бекенд' in position_lower_self or 'фронтендер' in position_lower_self)):
                raise ValidationError("Тестировщики и разработчики не могут сидеть за соседними столами.")
