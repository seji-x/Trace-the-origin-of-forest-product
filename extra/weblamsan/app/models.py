from django.db import models

# Create your models here.
class Producer (models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    infor = models.CharField(max_length=250)
class Transporters (models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    infor = models.CharField(max_length=250)
class Owner (models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    infor = models.CharField(max_length=250)
class Wood (models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    transporters = models.ForeignKey(Transporters, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    size = models.IntegerField(max_length=250)
    age = models.IntegerField(max_length=250)
    status = models.CharField(max_length=250)
    def __str__(self):
        context = ["name: "+self.name,"kích thước: "+str(self.size),"tuổi: "+str(self.age),"trạng thái: "+self.status]
        result = " ".join(context)
        return result