from django.db import models

# Create your models here.
class Contact(models.Model):
    '''
    Model represents contact form
    '''
    full_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=150, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(blank=False)
    is_answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name