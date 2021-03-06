# Generated by Django 2.1 on 2019-06-29 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('year', models.CharField(max_length=10, verbose_name='Год издания')),
                ('file', models.FileField(blank=True, null=True, upload_to='book_files', verbose_name='Файл')),
                ('image', models.ImageField(blank=True, null=True, upload_to='book_images', verbose_name='Фотография')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='webapp.Author', verbose_name='Автор')),
            ],
        ),
    ]
