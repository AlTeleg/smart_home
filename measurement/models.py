from django.db import models


class Sensor(models.Model):
    class Meta:
        verbose_name = "sensor"

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

