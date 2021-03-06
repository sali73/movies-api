from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'title', 'photo', 'year', 'vedio', 'actors', 'director', 'rate']


class MoviesMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'title', 'photo', 'rate']
