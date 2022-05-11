from django.db import models


class City(models.Model):
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}, {self.region}"


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=255)
    region = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hospital_name},  {self.region.city}"


