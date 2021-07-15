from rest_framework import generics
from apps.users.api import serializers
from apps.users.models import Profile


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class ProfileDeleteAPIView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
