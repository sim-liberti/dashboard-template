from django.db import models
from django.contrib.auth.models import User

class Years(models.TextChoices):
    FIRST = "First", "First"
    SECOND = "Second", "Second"
    THIRD = "Third", "Third"

class Semesters(models.TextChoices):
    FIRST = "First", "First"
    SECOND = "Second", "Second"

class Booklet(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_number = models.CharField(max_length=9, null=True, blank=True)
    cf = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    total_exams = models.IntegerField(default=0, null=True)
    total_credits = models.IntegerField(default=0, null=True)

    setup_status = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.owner.username}'s booklet"

class Exam(models.Model):
    booklet = models.ForeignKey(Booklet, on_delete=models.CASCADE)
    code = models.CharField(primary_key=True, max_length=10, null=False)
    name = models.CharField(max_length=255, null=False)
    credits = models.IntegerField(default=0, null=False)
    year = models.CharField(max_length=10, choices=Years.choices, default=Years.FIRST, null=False)
    semester = models.CharField(max_length=10, choices=Semesters.choices, default=Semesters.FIRST, null=False)
    completion_date = models.DateField(null=True)
    completion_grade = models.IntegerField(null=True)
    cum_laude = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"