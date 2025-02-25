from django.db import models
from datetime import datetime

class Timeline(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.datetimefield(auto_now_add=True)
    timeline_start = models.DateTimeField()
    timeline_end = models.DateTimeField()

    def __str__(self):
        return f"Timeline {self.id}"

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.datetimefield(auto_now_add=True)
    timeline = models.OneToOneField(Timeline, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=600)

    def __str__(self):
        return f"Project {self.id}"
    
    def save(self, *args, **kwargs):
        #can optionally start with a timeline start and end date or not
        timeline_start, timeline_end = None
        if 'timeline_start' in kwargs:
            timeline_start = kwargs['timeline_start']
        else:
            timeline_start = datetime.now()
        if 'timeline_end' in kwargs:
            timeline_end = kwargs['timeline_end']

        if not self.timeline:
            # Create a new Timeline if one doesn't exist
            timeline = Timeline.objects.create(
                timeline_start=timeline_start,
                timeline_end=timeline_end,
            )
            self.timeline = timeline
        
        super().save(*args, **kwargs)

class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    timeline = models.OneToOneField(Timeline, on_delete=models.CASCADE)
    created_at = models.datetimefield(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    financial_impact= models.IntegerField()

    def __str__(self):
        return f"Event {self.name} ({self.id})"

class ProjectMember(models.Model):
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, db_index=True)
    user_id = models.IntegerField()#not unique
    role = models.CharField(max_length=255)

    def __str__(self):
        return f"Member {self.user_id} in Project {self.project.id}"