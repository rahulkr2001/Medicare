from django.db import models
class Doctor(models.Model):
    name=models.CharField(max_length=256)
    specialization=models.CharField(max_length=256)
    location=models.CharField(max_length=128)
    phone=models.CharField(max_length=10)
    mail=models.CharField(max_length=128)

    def __str__(self):
        return "{}".format(self.name)

class Patient(models.Model):
    name=models.CharField(max_length=256)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    gander=models.CharField(max_length=256)
    age=models.CharField(max_length=2)
    phone=models.CharField(max_length=10)
    mail=models.CharField(max_length=128)

    def __str__(self):
        return "{}".format(self.name)
