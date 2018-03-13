from django.contrib import admin
from .models import *


class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "code", "credits", "manager", "level", "taught_semester", "module_type")


admin.site.register(Module, ModuleAdmin)
admin.site.register(Programme)
admin.site.register(Accreditation)
admin.site.register(Criterion)