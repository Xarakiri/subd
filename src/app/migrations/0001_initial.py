# Generated by Django 3.2.9 on 2021-12-20 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255, verbose_name='Название дисциплины')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Имя')),
                ('surname', models.TextField(max_length=255, verbose_name='Фамилия')),
                ('patronomic', models.TextField(max_length=255, verbose_name='Отчество')),
                ('academic_rank', models.TextField(max_length=255, verbose_name='Ученое звание')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='преподаватель', to='app.disciplines')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='дисциплина', to='app.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255, verbose_name='Название факультета')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='app.teacher')),
            ],
        ),
    ]
