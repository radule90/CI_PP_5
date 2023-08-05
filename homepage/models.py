from django.db import models

# Create your models here.


class Subscriber(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
