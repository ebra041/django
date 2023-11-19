from django.db import models
from django.utils.text import slugify

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    slug= models.SlugField(unique=True,max_length=40,blank=True)
    password = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fname + self.sname)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.fname + self.sname
