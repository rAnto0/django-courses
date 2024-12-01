from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm, LessonForm


def course_list(request):
    courses = Course.objects.all()  # Получаем все курсы
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)  # Получаем курс по ID
    lessons = course.lessons.all()  # Уроки этого курса
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user  # Привязываем курс к текущему пользователю
            course.save()
            return redirect('course_list')  # Перенаправляем на страницу со списком курсов
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})


def add_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course  # Привязываем урок к выбранному курсу
            lesson.save()
            return redirect('course_detail', pk=course.id)  # Перенаправляем на страницу курса
    else:
        form = LessonForm(initial={'course': course})
    return render(request, 'courses/add_lesson.html', {'form': form, 'course': course})
