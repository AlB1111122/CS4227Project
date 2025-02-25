from project_service.models import *
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from datetime import datetime

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
    
    def create(self, validated_data):
        if validated_data.get('timeline') == None:
            timeline_start = validated_data.pop('timeline_start', datetime.now())
            timeline_end = validated_data.pop('timeline_end', datetime.max)

            timeline = Timeline.objects.create(
                timeline_start=timeline_start,
                timeline_end=timeline_end
            )
            validated_data.pop('timeline') 

        project = Project.objects.create(
            **validated_data,
            timeline=timeline
        )
        return project

class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'
    
    def is_date_valid(timeline_start,timeline_end):
        if timeline_start >= timeline_end:
            raise ValidationError({
                'timeline_end': 'Timeline end must be after the start date.'
            })

    
    def create(self, validated_data):
        timeline_start = validated_data.pop('timeline_start')
        timeline_end = validated_data.pop('timeline_end')

        self.is_date_valid(timeline_start,timeline_end)

        timeline = Timeline.objects.create(
            **validated_data,
            timeline_start=timeline_start,
            timeline_end=timeline_end
        )
        return timeline

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'

class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = '__all__'
