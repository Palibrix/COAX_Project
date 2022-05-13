from django.db import models


class Cities(models.Model):
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}"



class Departments(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.name}"


class Doctor(models.Model):
    first_name = models.CharField('First name', max_length=255)
    surname = models.CharField('Surname', max_length=255)
    departament = models.ForeignKey(Departments,
                                    null=True,
                                    on_delete=models.SET_NULL)
    details = models.TextField('Work Experience', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"
# Why don't working many to many in hospital-departament
class Hospitals(models.Model):
    hospital_name = models.CharField(max_length=255)
    region = models.ForeignKey(Cities, on_delete=models.CASCADE)
    web = models.URLField('Website of Hospital', blank=True)
    departament = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE)
    doctors = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.hospital_name}"




