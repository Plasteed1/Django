from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
import datetime
from .models import Employee
def home(request):
    total_employees = Employee.objects.count()
    latest_employees = Employee.objects.order_by('-start_date')[:4]

    for emp in latest_employees:
        emp.experience_days = emp.experience_days
        first_image_obj = emp.images.first()
        emp.first_image_url = first_image_obj.image.url if first_image_obj else None

    context = {
        'total_employees': total_employees,
        'latest_employees': latest_employees,
    }
    return render(request, 'employees/home.html', context)


def employee_list(request):
    employees_qs = Employee.objects.all().order_by('last_name')
    paginator = Paginator(employees_qs, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for emp in page_obj:
        emp.experience_days = emp.experience_days
        first_image_obj = emp.images.first()
        emp.first_image_url = first_image_obj.image.url if first_image_obj else None

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'employees/employee_list.html', context)
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    experience_days = employee.experience_days
    images_qs = employee.images.all()
    main_image_url = images_qs.first().image.url if images_qs.exists() else None
    gallery_images = images_qs[1:]
    context = {
        'employee': employee,
        'experience_days': experience_days,
        'main_image_url': main_image_url,
        'gallery_images': gallery_images,
    }
    return render(request, 'employees/employee_detail.html', context)
