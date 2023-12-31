from rest_framework import serializers

from src.apps.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = ("pk", "title", "start", "end", "owner", "meeting_link")
