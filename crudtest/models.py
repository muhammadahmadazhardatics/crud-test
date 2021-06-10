from django.db import models

class Crud(models.Model):
    name = models.CharField(verbose_name="First Name", max_length=30)
    email = models.EmailField(verbose_name="Email Address", max_length=30)

    def __str__(self):
        return self.name
