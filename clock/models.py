from django.db import models
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    class DaysOfWeek(models.TextChoices):
        MONDAY = 'MON', _('Monday')
        TUESDAY = 'TUE', _('Tuesday')
        WEDNESDAY = 'WED', _('Wednesday')
        THURSDAY = 'THU', _('Thursday')
        FRIDAY = 'FRI', _('Friday')
        SATURDAY = 'SAT', _('Saturday')
        SUNDAY = 'SUN', _('Sunday')

    class PriorityLevel(models.IntegerChoices):
        LOW = 1, _('Low')
        MEDIUM = 2, _('Medium')
        HIGH = 3, _('High')

    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        IN_PROGRESS = 'IN_PROGRESS', _('In Progress')
        COMPLETED = 'COMPLETED', _('Completed')

    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    steps = models.TextField(blank=True)
    repeat = models.CharField(
        max_length=3, 
        choices=DaysOfWeek.choices, 
        blank=True, 
        help_text=_("Repeat task on this day of the week.")
    )
    priority = models.IntegerField(
        choices=PriorityLevel.choices, 
        default=PriorityLevel.MEDIUM
    )
    status = models.CharField(
        max_length=12, 
        choices=Status.choices, 
        default=Status.PENDING
    )
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title