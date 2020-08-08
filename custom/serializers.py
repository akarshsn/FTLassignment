from rest_framework import serializers
from .models import User,Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['start_time','end_time']


class UserSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)
    class Meta:
        model  = User
        fields = ['id', 'real_name', 'tz', 'activities']

