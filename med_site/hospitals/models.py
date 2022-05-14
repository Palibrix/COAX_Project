from django.db import models


class Cities(models.Model):
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}, {self.region}"

    class Meta:
        ordering = ("-region", )


class Hospitals(models.Model):
    hospital_name = models.CharField(max_length=255)
    region = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hospital_name},  {self.region.city}"

    class Meta:
        ordering = ("-region", )


class Departments(models.Model):
    name = models.CharField(max_length=255)
    hospital_name = models.ForeignKey(Hospitals, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.hospital_name}"

    class Meta:
        ordering = ('-hospital_name',)
