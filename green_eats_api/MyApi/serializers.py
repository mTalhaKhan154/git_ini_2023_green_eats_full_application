from django.contrib.auth.models import User, Group
from rest_framework import serializers
from MyApi.models import getData

class ImageRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = getData
        fields = "__all__"#['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']