from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # Главная страница курсов
    path('<int:pk>/', views.course_detail, name='course_detail'),  # Детали курса
    path('add/', views.add_course, name='add_course'),  # Страница добавления курса
    path('<int:course_id>/add_lesson/', views.add_lesson, name='add_lesson'),  # Добавить урок
]
