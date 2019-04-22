from rest_framework import serializers


class AddressSerializer(serializers.Serializer):

    def to_representation(self, obj):
        return obj.as_dict()
