from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
# Create your models here.

STATUS = (
    ("AC", "Active"),
    ("AL", "Alumnae"),
    ("DE", "Deceased"),
)

NICKNAME_STATUS = (
    ("AP", "Approved"),
    ("QU", "Queued"),
    ("DE", "Denied"),
)


class Chapter(models.Model):
    name = models.CharField(max_length=50)
    chapter_school = models.CharField(max_length=50)
    city_state = models.CharField(max_length=50)
    original_founding_date = models.DateField()
    recharter_date = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse('chapter_detail', kwargs={'pk': self.id})


class Sister(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    nickname = models.CharField(max_length=20)
    nickname_meaning = models.TextField(max_length=250)
    chapter = models.CharField(
        max_length=10,
        # choices=Chapter,
        default="null")
    crossing_chapter = models.CharField(
        max_length=10,
        # choices=Chapter,
        default="null")
    crossing_semester = models.CharField(max_length=6)
    crossing_year = models.IntegerField()
    big_sister = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    little_sister_crossed = models.ManyToManyField(
        'self', blank=True)
    tree = models.CharField(max_length=20)
    line_number = models.IntegerField(null=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=STATUS[0][0])

    def __str__(self):
        return self.nickname


class Pnm(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    chapter = models.CharField(
        max_length=10,
        # choices=Chapter,
        default="null")
    process_chapter = models.CharField(
        max_length=10,
        # choices=Chapter,
        default="null")
    process_semester = models.CharField(max_length=6)
    process_year = models.PositiveSmallIntegerField()
    potential_line_number = models.PositiveSmallIntegerField()
    big_sister = models.ForeignKey(Sister, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"PNM {self.first_name}"


class Nickname_Request (models.Model):
    name = models.CharField("nickname request", max_length=20,)
    nickname_meaning = models.TextField(max_length=250)
    pnm = models.ForeignKey(Pnm, on_delete=models.CASCADE, null=True)
    requestor: models.ForeignKey(Sister, on_delete=models.CASCADE, null=True)
    req_date = models.DateTimeField('date requested')
    nickname_status: models.CharField(
        max_length=2,
        choices=NICKNAME_STATUS,
        default="null")

    def was_requested_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.req_date <= now

    # def get_absolute_url(self):
    #     return reverse('chapter_detail', kwargs={'pk': self.id})

    #     def get_absolute_url(self):
    #         return reverse('toys_detail', kwargs={'pk': self.id})

    # # Add the foreign key linking to a user instance
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'cat_id': self.id})

    #     def __str__(self):
    #         return f"{self.get_meal_display()} on {self.date}"

    #     # change the default sort
    #     class Meta:
    #         ordering = ['-date']