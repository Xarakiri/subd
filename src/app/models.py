from django.db import models


class Teacher(models.Model):
    name = models.TextField(verbose_name='Имя', max_length=255)
    surname = models.TextField(verbose_name='Фамилия', max_length=255)
    patronomic = models.TextField(verbose_name='Отчество', max_length=255)
    academic_rank = models.TextField(verbose_name='Ученое звание', max_length=255)

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronomic} ({self.academic_rank})'


class Disciplines(models.Model):
    title = models.TextField(verbose_name='Название дисциплины', max_length=255)

    def __str__(self):
        return self.title


class Faculties(models.Model):
    title = models.TextField(verbose_name='Название факультета', max_length=255)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='faculties')

    def __str__(self):
        return f'{self.title} - {self.teacher_id}'


class TeacherDiscipline(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='дисциплина')
    discipline_id = models.ForeignKey(Disciplines, on_delete=models.CASCADE, related_name='преподаватель')

    def __str__(self) -> str:
        return f'{self.teacher_id} преподает {self.discipline_id}'
