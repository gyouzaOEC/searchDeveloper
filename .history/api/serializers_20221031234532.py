from rest_framework import serializers
from proj.models import Project,Tag,Profile
from users.models import 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


