from django.db import models

class RoadSegment(models.Model):
    id = models.AutoField(primary_key=True)
    long_start = models.FloatField(default=0.0)
    lat_start = models.FloatField(default=0.0)
    long_end = models.FloatField(default=0.0) 
    lat_end = models.FloatField(default=0.0)
    length = models.FloatField(default=0.0)
    speed = models.FloatField(default=0.0)


    @property
    def intensity(self):
        if self.speed <= 20:
            return 'elevada'
        elif self.speed <= 50:
            return 'média'
        else:
            return 'baixa'
