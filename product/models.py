from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.datetime.now)
    image = models.ImageField(default='default.jpg', upload_to='post_image/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

#чтобы прописывать таблицы в базе данных
