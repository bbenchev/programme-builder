from django.db import models
from django.contrib.auth.models import User

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
    code = models.CharField(max_length=15, default="10")
    credits = models.CharField(max_length=2)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default="00")
    taught_semester = models.CharField(max_length=1)
    module_type = models.CharField(max_length=1, choices=MODULE_TYPES,
        default=COMPULSORY, blank=False)
    level = models.CharField(max_length=1)
    prerequisites = models.ManyToManyField('self', symmetrical=False,
        related_name='is_prerequisite_of')

    def __str__(self):
        return self.code + " " + self.title

class Programme(models.Model):
    name = models.CharField(max_length=100)
    ucas_code = models.CharField(max_length=10)
    level = models.IntegerField(default=7)
    years = models.CharField(max_length=1, default=3)
    modules = models.ManyToManyField(Module, related_name='programmes')

    def __str__(self):
        return self.name


class Criterion(models.Model):
    code = models.CharField(max_length=10)
    definition = models.TextField()
    is_met_by = models.ManyToManyField(Module, related_name="meets")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = "Criteria"


class Accreditation(models.Model):
    # IET, QAA
    name = models.CharField(max_length=20)
    criteria = models.ManyToManyField(Criterion, related_name='accreditations')
    programmes = models.ManyToManyField(Programme, related_name='is_accredited_by')

    def __str__(self):
        return self.name






