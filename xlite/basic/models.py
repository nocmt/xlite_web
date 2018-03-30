from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=70, verbose_name="标题")
    body = models.TextField(verbose_name="正文")
    cover = models.CharField(max_length=300, blank=True, verbose_name="封面")
    created_time = models.DateTimeField(default=timezone.now, verbose_name="时间")

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('basic:article', kwargs={'pk': self.pk})