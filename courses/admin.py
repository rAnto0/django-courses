from django.contrib import admin
from .models import UserProfile, Course, Lesson, Progress

admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Progress)
