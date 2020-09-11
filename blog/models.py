from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):

    class Meta:
        db_table = 'post'
        verbose_name = 'Стаття'
        verbose_name_plural = "Статті"
        ordering = ['create']

    title = models.CharField("Заголовок", max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    text = models.TextField("Текст статті", max_length=2500)
    image = models.ImageField("Зображення", upload_to="images/", blank=True)
    create = models.DateTimeField("Створенно", auto_now_add=True)
    update = models.DateTimeField("Обновленно", auto_now=True)
    moderation = models.BooleanField("Модерація", default=False)

    tags = TaggableManager()

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.title

