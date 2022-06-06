from django.db import models
from django.contrib.auth.models import User


class AttemptsManager(models.Manager):
    def get_queryset(self):
        return super(AttemptsManager, self).get_queryset().all()


class AdoptedManager(models.Manager):
    def get_queryset(self):
        return super(AdoptedManager, self).get_queryset().filter(verdict=1)


class Problem(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    difficulty = models.IntegerField()
    rating = models.FloatField(default=0)

    class Meta:
        abstract = True


class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    source_code = models.TextField()
    verdict = models.IntegerField(default=-2)
    created = models.DateTimeField(auto_now_add=True)

    objects = AttemptsManager()
    adopted = AdoptedManager()

    class Meta:
        abstract = True
