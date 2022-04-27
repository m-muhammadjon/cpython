from django.contrib import admin

from .models import Problem, ProgrammingLanguage, Employee, Department

admin.site.register(Problem)
admin.site.register(ProgrammingLanguage)
admin.site.register(Employee)
admin.site.register(Department)

# Register your models here.
