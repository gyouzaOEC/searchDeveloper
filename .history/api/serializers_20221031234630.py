from rest_framework import serializers
from proj.models import Project,Tag,Profile
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

class Serializer(serializers.ModelSerializer):

    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


