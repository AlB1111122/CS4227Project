from django.db import models

class Timeline(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    timeline_start = models.DateField()
    timeline_end = models.DateField()

    def __str__(self):
        return f"Timeline {self.id}"

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    timeline = models.OneToOneField(Timeline, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=600)

    def __str__(self):
        return f"Project {self.id}"

class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return f"Event {self.name} ({self.id})"

class ProjectMember(models.Model):
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, db_index=True)
    user_id = models.IntegerField()#not unique
    role = models.CharField(max_length=255)

    def __str__(self):
        return f"Member {self.user_id} in Project {self.project.id}"