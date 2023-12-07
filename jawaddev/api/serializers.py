from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post, PostCategory
from user.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    profile = serializers.SerializerMethodField()  

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'date_joined', 'profile']  

    def get_profile(self, obj):
        try:
            profile = obj.profile
            return ProfileSerializer(profile).data
        except Profile.DoesNotExist:
            return None

class PostCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    categories = PostCategorySerializer(many=True) 

    class Meta:
        model = Post
        fields = ['id', 'slug', 'title', 'content', 'thumbnail', 'published_date', 'updated_date', 'is_published', 'word_count', 'reading_time', 'author', 'categories']   