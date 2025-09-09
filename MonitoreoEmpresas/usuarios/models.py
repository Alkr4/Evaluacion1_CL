from django.db import models
from dispositivos.models import BaseModel
# Create your models here.

class User(BaseModel):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    organization = models.ForeignKey('dispositivos.Organization', on_delete=models.CASCADE)

    def __str__(self):
        return self.email