from django.db import models

class Timeline(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    timeline_start = models.DateField()
    timeline_end = models.DateField()

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    timeline = models.OneToOneField(Timeline, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=600)

class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    timeline = models.OneToOneField(Timeline, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    financial_impact= models.IntegerField()
    document_id = models.IntegerField(blank=True, null=True)

class ProjectMember(models.Model):
    class Role(models.TextChoices):
        OWNER = 'OWNER'
        EDITOR = 'EDITOR'
        VIEWER = 'VIEWER'

    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, db_index=True)
    user_id = models.IntegerField()#not unique
    role = models.CharField(max_length=255,choices=Role.choices,default=Role.VIEWER, blank=True)
