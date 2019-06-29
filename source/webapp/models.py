from django.db import models
from django.urls import reverse

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

