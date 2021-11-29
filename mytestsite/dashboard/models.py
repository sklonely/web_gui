# Create your models here.
from django.db import models


class Post(models.Model):
    
    machine_name = models.CharField(max_length=100, primary_key=True)
    work_no = models.CharField(max_length=100,null=True)
    principal = models.CharField(max_length=100,null=True)

    production_capacity = models.DecimalField(max_digits=10,decimal_places=0,null=True)
    need_production_capacity = models.DecimalField(max_digits=10,decimal_places=0,null=True)
    check_nums = models.DecimalField(max_digits=10,decimal_places=0,null=True)
    speed = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    good_production = models.DecimalField(max_digits=10,decimal_places=0,null=True)

    fiex_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.machine_name