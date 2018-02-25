from django.db import models

class Module(models.Model):
    COMPULSORY = "C"
    OPTIONAL = "O"
    DISCOVERY = "D"
    MODULE_TYPES = (
        (COMPULSORY, "Compulsory"),
        (OPTIONAL, "Optional"),
        (DISCOVERY, "Discovery")
    )
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=15)
    credits = models.CharField(max_length=2)
    taught_semester = models.CharField(max_length=1)
    module_type = models.CharField(max_length=1, choices=MODULE_TYPES,
        default=COMPULSORY, blank=False)
    level = models.CharField(max_length=1)
    prerequisites = models.ManyToManyField('self', symmetrical=False,
        related_name='is_prerequisite_of')

    def __str__(self):
        return self.title

class Programme(models.Model):
    name = models.CharField(max_length=100)
    ucas_code = models.CharField(max_length=10)
    years = models.CharField(max_length=1, default=3)
    modules = models.ManyToManyField(Module, related_name='programmes')

    def __str__(self):
        return self.name


class Criterion(models.Model):
    code = models.CharField(max_length=10)
    definition = models.TextField()

    def __str__(self):
        return self.code


class Accreditation(models.Model):
    name = models.CharField(max_length=20)
    criteria = models.ManyToManyField(Criterion, related_name='accreditations')

    def __str__(self):
        return self.name






