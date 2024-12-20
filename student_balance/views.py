from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import date
from .models import Student, Category


def student_list(request):
    students = Student.objects.all()
    for student in students:
        student.update_balance()
    return render(request, 'student_balance/student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_balance/student_detail.html', {'student': student})


def add_student(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        start_date = request.POST.get('start_date')
        category_id = request.POST.get('category')

        category = get_object_or_404(Category, id=category_id)
        start_date = date.fromisoformat(start_date)

        student = Student(
            first_name=first_name,
            last_name=last_name,
            start_date=start_date,
            category=category,
        )
        student.update_balance()
        student.save()
        return redirect('student_list')

    return render(request, 'student_balance/add_student.html', {'categories': categories})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'student_balance/category_list.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        balance = request.POST.get('balance')

        category = Category(
            name=name,
            balance=int(balance),
        )
        category.save()
        return redirect('category_list')

    return render(request, 'student_balance/add_category.html')


def update_balances_view(request):
    students = Student.objects.all()
    for student in students:
        student.update_balance()
    return HttpResponse("All student balances have been updated!")