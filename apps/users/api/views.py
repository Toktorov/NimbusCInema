from rest_framework import generics
from apps.users.api import serializers
from apps.users.models import Profile


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
