from django.db import models

'''
Category => title, slug
Tag => title, slug
Post => title, slug, content, author, created_at, photo, views, category, tags
'''


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименовании Категории")
    slug = models.SlugField(max_length=255, verbose_name='УРЛС', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименовании Тега")
    slug = models.SlugField(max_length=50, verbose_name='УРЛС', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']



class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование новости")
    slug = models.SlugField(max_length=50, unique=True)
    author = models.CharField(max_length=100, verbose_name="Автор")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фотография")
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    # is_published = models.BooleanField(default=False, verbose_name='Статус')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts", verbose_name="Категория")
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts", verbose_name="Тег")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


