from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.email}'


class ContactLink(models.Model):
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class About(models.Model):
    text = RichTextField()
    mini_text = RichTextField()


class ImageAbout(models.Model):
    """класс модели изображений о нас"""

    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='abot_images')


class Social(models.Model):
    """"класс моделей соцсетей страницы о нас"""

    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField()