from rest_framework import serializers
from django.contrib.auth.models import User

from taggit.models import Tag

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    name = serializers.ReadOnlyField(source='user.username')
    admin = serializers.ReadOnlyField(source='is_company_admin')

    class Meta:
        model = Profile
        fields = ['id', 'name', 'admin']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class TagSerializerField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return data.values_list('name', flat=True)


class UserTagSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    tags = TagSerializerField()

    class Meta:
        model = Profile
        fields = ['user', 'tags']

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(TagSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance
