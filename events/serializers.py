from rest_framework import serializers

from app.models import Event


class EventSerializer(serializers.ModelSerializer):
    """Serializer for Event object"""

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'conducted_by', 'created_date', 'image')
        read_only_Fields = ('id',)
