from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    # при создании будет выставлена тек.дата - auto_now_add=True
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'