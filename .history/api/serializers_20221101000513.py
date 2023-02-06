from rest_framework import serializers
from proj.models import Project,Tag,Profile,Review
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

    
class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=False)
    
    class Meta:
        model = Project
        fields = "__all__"


