# core/serializers.py

from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("id", "name", "definition", "video", "genre", "prep_time", "country")