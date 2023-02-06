from rest_framework import serializers
from proj.models import Project,Tag,Profile,Review
from users.models import Profile

        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
        
class ProfileSerializer(serializers.ModelSerializer):
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
    reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = "__all__"

    def get_reviews(self,obj):
        reviews = obj.review_set.all()
        serializer = Reve
        return 
