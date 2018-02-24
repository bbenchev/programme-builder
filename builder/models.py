from django.db import models

class Module(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=15)
    credits = models.CharField(max_length=2)
    taught_semester = models.CharField(max_length=1)
    module_type = models.CharField(max_length=30)
    level = models.CharField(max_length=1)

    def __str__(self):
        return self.title

class Programme(models.Model):
    name = models.CharField(max_length=100)
    ucas_code = models.CharField(max_length=10)
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return self.name






