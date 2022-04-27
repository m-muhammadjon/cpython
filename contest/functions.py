# Contest 162
from django.db.models.functions import Length

from .models import Employee

from django.db.models import Model, QuerySet, Q
from django.db.models import Max


# A
def get_problems(Problem: Model) -> QuerySet:
    return Problem.objects.all()


# B
def get_first(Problem: Model):
    return Problem.objects.first()


# C
def get_problems(Problem: Model) -> QuerySet:
    return Problem.objects.filter(difficulty=1)


# D
def get_problems(Problem: Model) -> QuerySet:
    return Problem.objects.filter(rating__gt=4)


# E
def get_problems(Problem: Model) -> QuerySet:
    return Problem.objects.filter(rating__gte=4, rating__lte=5) | Problem.objects.filter(difficulty=2)


# F
def get_last(Problem: Model):
    return Problem.objects.filter(~Q(rating__gte=2, rating__lte=4)).last()


# G
def get_problems_count(Problem: Model) -> int:
    pr = Problem.objects.values_list('rating', flat=True)
    return len(set(pr))


# H
def get_problems(Problem: Model) -> QuerySet:
    return Problem.objects.filter(rating__in=[1, 2, 3, 4, 5]).order_by('difficulty')


# I
def get_problems(Problem: Model) -> QuerySet:
    return Problem.objects.filter(title__startswith='A')


# J
def get_problems(Problem: Model) -> QuerySet:
    max = Problem.objects.aggregate(Max('rating'))['rating__max']
    return Problem.objects.filter(rating=max)


# K
def get_problems(Problem: Model) -> QuerySet:
    max = Problem.objects.annotate(body_cnt=Length('body')).aggregate(Max('body_cnt'))
    return Problem.objects.annotate(body_cnt=Length('body')).filter(body_cnt=max['body_cnt__max'])


# L
def get_languages(ProgrammingLanguage: Model) -> QuerySet:
    return ProgrammingLanguage.languages.all()


# M
def get_languages(ProgrammingLanguage: Model) -> QuerySet:
    return ProgrammingLanguage.languages.filter(name__exact='Python')


# N
def get_languages(ProgrammingLanguage: Model) -> QuerySet:
    return ProgrammingLanguage.languages.filter(name__in=['Python', 'C++'])


# O
def get_languages(ProgrammingLanguage: Model) -> QuerySet:
    max = ProgrammingLanguage.languages.annotate(cnt=Length('name')).aggregate(Max('cnt'))
    return ProgrammingLanguage.languages.annotate(cnt=Length('name')).filter(cnt=max['cnt__max'])


# P
def get_first_employee(Employee: Model):
    return Employee.employees.first()


# Q
def get_old_employees(Employee: Model) -> QuerySet:
    return Employee.employees.filter(age__gte=40)


# R
def get_employees(Employee: Model) -> QuerySet:
    return Employee.employees.filter(department__floor__gte=1, department__floor__lte=9)


# S
def get_old_employees(Employee: Model) -> QuerySet:
    qs = Employee.employees.values('id', 'first_name', 'last_name')
    ids = []
    for x in qs:
        if x['first_name'] == x['last_name']:
            ids.append(x['id'])
    return Employee.employees.filter(id__in=ids)


# T
def get_employees(Employee: Model) -> QuerySet:
    qs = Employee.employees.all()
    ids = [x.id for x in qs if int(x.age ** 1 / 2) * int(x.age ** 1 / 2) == x.age]
    return Employee.employees.filter(id__in=ids)


# U
def get_old_employees(Employee: Model) -> QuerySet:
    qs = Employee.employees.all()
    vowel = ['a', 'e', 'i', 'o', 'u']
    ids = []
    for x in qs:
        for i in x.first_name:
            if i in vowel:
                ids.append(x.id)
                break
    return Employee.employees.filter(id__in=ids)
