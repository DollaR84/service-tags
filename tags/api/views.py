from rest_framework import generics, permissions

from rest_framework.response import Response

from rest_framework.views import APIView

from django.contrib.auth.models import User

from taggit.models import Tag

from .models import Profile

from . import serializers

from .permissions import IsUser, IsAdmin, IsUserOrAdmin, IsAdminUserOrReadOnly

# Create your views here.


class TagsList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UsersList(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get_queryset(self):
        tags = self.kwargs.get('tags')
        if tags:
            tags = tags.split('+')
            return Profile.objects.filter(tags__name__in=tags).distinct()
        else:
            return Profile.objects.all()


class UserTag(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.UserTagSerializer
    permission_classes = [permissions.IsAuthenticated, IsUserOrAdmin]

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk:
            return self.queryset.get(user=pk)
        else:
            return self.queryset.get(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save()
        if 'tags' in self.request.DATA:
            instance.tags.set(*self.request.DATA['tags'])
