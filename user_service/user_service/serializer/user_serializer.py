from rest_framework import serializers
from user_service.model.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'