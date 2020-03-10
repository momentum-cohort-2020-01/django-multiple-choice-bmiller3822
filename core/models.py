import datetime
from django.db import models
from django.utils.text import slugify
from users.models import User

Categories = (
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JavaScript', 'JavaScript'),
    ('JSON', 'JSON'),
    ('AJAX', 'AJAX'),
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('Java', 'Java'),
    ('C#', 'C#'),
    ('Ruby', 'Ruby'),
    ('Rails', 'Rails'),
    ('C++', 'C++'),
    ('C', 'C'),
)


class Snippet(models.Model):
    snippet_title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    description = models.TextField()
    code = models.TextField()
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Snippet title: {self.snippet_title} Language: {self.language} Description: {self.description} Category: {self.category} Code: {self.code} '

    # class Meta:
    #     ordering = ['-created_at']


class Category(models.Model):
    category_name = models.CharField(max_length=100, choices=Categories)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.category_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)


class Library(models.Model):
    snippet = models.ForeignKey(
        Snippet, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return f'Snippet: {self.snippet.pk}'


# class User(AbstractUser):
#     pass
