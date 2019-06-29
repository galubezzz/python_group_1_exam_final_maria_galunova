from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=90, verbose_name="ФИО")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    date_of_death = models.DateField(blank=True, null=True, verbose_name='Дата смерти')
    biography = models.TextField(max_length=5000, null=True, blank=True, verbose_name='Биография')
    image = models.ImageField(upload_to='author_images', blank=True, null=True, verbose_name="Фотография")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('webapp:author_details', kwargs={'pk': self.pk})


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.ForeignKey(Author, related_name="books", verbose_name="Автор", on_delete=models.CASCADE)
    year = models.CharField(max_length=10, verbose_name="Год издания")
    file = models.FileField(upload_to='book_files', blank=True, null=True, verbose_name="Файл")
    image = models.ImageField(upload_to='book_images', blank=True, null=True, verbose_name="Фотография")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Текст отзыва")
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время создания")
    book = models.ForeignKey(Book, related_name="reviews", blank=True, verbose_name="Книга", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('webapp:book_details', kwargs={'pk': self.book.id})

    def __str__(self):
        return f"{self.pk}. {self.text} | {self.author.username}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
