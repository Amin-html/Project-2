from django.db import models

class Computer(models.Model):
    ZONE_CHOICES = [
        ('standard', 'Стандартная зона'),
        ('vip', 'VIP зона'),
        ('gaming', 'Игровая зона'),
    ]
    name = models.CharField(max_length=100)
    zone = models.CharField(max_length=25, choices=ZONE_CHOICES)
    cpu = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100)
    ram = models.IntegerField()
    price_per_hour = models.IntegerField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='computers/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.get_zone_display()})'
# Create your models here.
