from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Korisnik(AbstractUser):
    ROLES = (('prof', 'profesor'), ('stu', 'student'),('adm','admin'))
    STATUS = (('none', 'None'), ('izv', 'izvanredni student'), ('red', 'redovni student'))
    role = models.CharField(max_length=50, choices=ROLES)
    status = models.CharField(max_length=50, choices=STATUS)

    

class Predmeti(models.Model):
    IZBORNI = (('DA', 'da'), ('NE', 'ne'))
    name = models.CharField(max_length=50)
    kod = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    izborni = models.CharField(max_length=50, choices=IZBORNI)
    nositelj =models.ForeignKey(Korisnik,on_delete=models.CASCADE, blank=True,null=True)   

    def __str__(self):
        return self.name
    def delete(self,*args,**kwargs):
        self.address.delete()
        super().delete(*args,**kwargs)

class Upisi(models.Model):
    STATUS = (('up', 'upisan'), ('pass', 'polozen'), ('fail', 'izgubio potpis'))
    user_id = models.ForeignKey(Korisnik, on_delete = models.CASCADE,blank=True,null=True)
    predmet_id = models.ForeignKey(Predmeti, on_delete = models.CASCADE, blank=True,null=True)
    status = models.CharField(default='up',max_length=50, choices=STATUS)
    


