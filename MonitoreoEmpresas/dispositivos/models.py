from django.db import models

class BaseModel(models.Model):
    states = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Organization(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Category(BaseModel):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Zone(BaseModel):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Device(BaseModel):
    name = models.CharField(max_length=255)
    max_value_threshold = models.FloatField()
    min_value_threshold = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Measurement(BaseModel):
    value = models.FloatField()
    timestamp = models.DateTimeField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.value
    
class Alert(BaseModel):
    severity_choices = [
        ("Baja", "BAJA"),
        ("Media", "MEDIA"),
        ("Alta", "ALTA"),
    ]
    severity = models.CharField(max_length=255, choices=severity_choices, default="Media")
    value = models.FloatField()
    timestamp = models.DateTimeField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.severity
    
