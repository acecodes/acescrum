from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Team(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class TeamRole(models.Model):

    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class TeamMember(models.Model):

    member = models.ForeignKey(Member)
    role = models.ForeignKey(TeamRole)
    team = models.ForeignKey(Team)


class Sprint(models.Model):

    """Development iteration period"""

    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end


class Task(models.Model):

    """Unit of work to be done for a sprint."""

    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, _('Not Started')),
        (STATUS_IN_PROGRESS, _('In Progress')),
        (STATUS_TESTING, _('Testing')),
        (STATUS_DONE, _('Done')),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    sprint = models.ForeignKey(Sprint, blank=True, null=True)
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
