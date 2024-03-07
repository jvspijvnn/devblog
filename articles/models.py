from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    thumbnail = models.ImageField(upload_to='assets')
    slug = models.SlugField()
    title = models.CharField(max_length=75)
    content = models.TextField()
    author = models.CharField(max_length=50, default='Mohamed Abdoul Aziz Seck')

    def get_absolute_url(self):
        return reverse("details", kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} {self.id}'

class commentaire(models.Model):
    objet = models.CharField(max_length=50)
    content = models.TextField()
    post = models.ForeignKey(Post,related_name= 'comments', on_delete=models.CASCADE)
