from rest_framework import serializers
from a_profile.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    absolute_profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'profile_picture','absolute_profile_picture_url','user']

    def get_absolute_profile_picture_url(self, obj):
        request = self.context.get('request')
        if obj.profile_picture and request:
            return request.build_absolute_uri(obj.profile_picture.url)
        return None
    
    def to_representation(self, instance):
        representation=super().to_representation(instance)
        representation["user"]=instance.user.username
        return representation