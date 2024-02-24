from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.CharField(max_length=255)



    def __str__(self) -> str:
        return self.name