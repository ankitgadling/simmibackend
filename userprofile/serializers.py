from .models import userprofile
from rest_framework.serializers import ModelSerializer


class userprofileserializers(ModelSerializer):
    class Meta:
        model = userprofile
        fields = ['id','profile_pics', 'created_at','user']
    
    def create(self, validated_data):
        return userprofile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.profile_pics = validated_data.get('profile_pics', instance.profile_pics)
        instance.save()  
        return super().update(instance, validated_data)