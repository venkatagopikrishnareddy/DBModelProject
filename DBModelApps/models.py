from django.db import models
class Employee(models.Model):
    eno=models.IntegerField();
    ename=models.CharField(max_length=30);
    esal=models.FloatField();
    eaddr=models.CharField(max_length=30);
    def __str__(self):
        s=str(self.eno)+'\t'+self.ename+'\t'+str(self.esal)+'\t'+self.eaddr;
        return s;

from django.db import models
class Job(models.Model):
    postdate=models.DateField();
    loc=models.CharField(max_length=30);
    offerdsal=models.IntegerField();
    qualification=models.CharField(max_length=30);

# Create your models here.
