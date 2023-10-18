from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)  # при удалении категории подкатегория не удалится, нулл=Тру и бланк=Тру значит что

    # подкатегория необязательна

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=220)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True,
    )
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=1)
    cook_time = models.PositiveIntegerField(default=1)
    ingredients = models.TextField(verbose_name='Ингридиенты')
    directions = models.TextField()
    post = models.ForeignKey(
        Post,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE, )
