from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Employee


class AllTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.employee = Employee.objects.create(
            first_name='Петр',
            last_name='Петров',
            gender='M',
            skills={'Python': 'Высокий'},
            start_date='2021-06-01',
            desk_number=5,
        )

        self.employee_for_access = Employee.objects.create(
            first_name='Иван',
            last_name='Иванов',
            gender='M',
            skills={},
            start_date='2020-01-01',
            desk_number=10,
        )

    def test_addresses_and_access(self):
        response_home = self.client.get(reverse('home'))
        self.assertEqual(response_home.status_code, 200)

        response_list = self.client.get(reverse('employee_list'))
        self.assertEqual(response_list.status_code, 200)

        url_detail = reverse('employee_detail', args=[self.employee_for_access.pk])
        response_detail = self.client.get(url_detail)
        self.assertEqual(response_detail.status_code, 200)

    def test_context_data(self):
        response = self.client.get(reverse('employee_detail', args=[self.employee.pk]))
        self.assertContains(response, 'Петр')
        experience_days = response.context['employee'].experience_days
        self.assertIsNotNone(experience_days)

    def test_validator_blocks_neighbors_for_testers_and_developers(self):
        tester = Employee.objects.create(
            first_name='Тестировщик',
            last_name='Тестов',
            gender='F',
            skills={},
            start_date='2022-01-01',
            desk_number=1,
            position='Тестировщик'
        )

        developer = Employee(
            first_name='Бекендер',
            last_name='Разработчик',
            gender='M',
            skills={},
            start_date='2022-01-01',
            desk_number=2,
            position='Бэкенд разработчик'
        )

        with self.assertRaises(ValidationError):
            developer.full_clean()

    def test_validator_allows_non_conflicting_positions(self):
        employee3 = Employee(
            first_name='Дизайнер',
            last_name='Дизайнерович',
            gender='F',
            skills={},
            start_date='2022-01-01',
            desk_number=2,
            position='Дизайнер'
        )

        try:
            employee3.full_clean()
        except ValidationError:
            self.fail("ValidationError raised unexpectedly!")
