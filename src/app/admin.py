from django.contrib import admin
from .models import Teacher, Disciplines, Faculties, TeacherDiscipline


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name', 'surname', 'patronomic', 'academic_rank']


@admin.register(Disciplines)
class DisciplinesAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Faculties)
class FacultiesAdmin(admin.ModelAdmin):
    search_fields = ['title', 'teacher_id']


@admin.register(TeacherDiscipline)
class TeacherDisciplineAdmin(admin.ModelAdmin):
    search_fields = ['teacher_id', 'discipline_id']
