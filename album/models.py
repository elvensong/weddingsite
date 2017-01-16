from django.db import models

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos')
    caption = models.CharField(max_length=200, blank = True)
    uploaded_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
