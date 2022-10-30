from rest_framework import serializers
from MailService.models import AccountHolder, TransactionsDetails, Recommendations


class AccountHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountHolder
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionsDetails
        fields = "__all__"


class RecommendationSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.time = validated_data.get("time", instance.time)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

    def create(self, validated_data):
        return Recommendations.objects.create(**validated_data)

    time = serializers.DateTimeField()
    description = serializers.CharField(max_length=100)
