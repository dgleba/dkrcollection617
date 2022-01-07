from rest_framework import serializers

from . import models


class bookmkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bookmk
        fields = [
            "bhash",
            "description",
            "comment",
            "url",
            "title",
            "created_at",
            "updated_at",
        ]
