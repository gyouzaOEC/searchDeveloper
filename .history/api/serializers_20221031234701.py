from rest_framework import serializers
from proj.models import Project,Tag,Profile
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiel
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


