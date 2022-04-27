from django.db import models


# Create your models here.
class Problem(models.Model):
    class Difficulty(models.IntegerChoices):
        EASY = 1
        MEDIUM = 2
        HARD = 3

    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    difficulty = models.IntegerField(choices=Difficulty.choices)
    rating = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.id}. {self.title}'


class ProgrammingLanguage(models.Model):
    languages = models.Manager()
    name = models.CharField(max_length=255)


class Department(models.Model):
    deparments = models.Manager()
    name = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()


class Employee(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 1
        FEMALE = 2

    employees = models.Manager()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=Gender.choices)
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        related_name='employees',
        null=True
    )
    language = models.ForeignKey(
        to=ProgrammingLanguage,
        on_delete=models.CASCADE,
        related_name='employees',
        null=True
    )
