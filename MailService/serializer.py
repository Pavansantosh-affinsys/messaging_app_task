from rest_framework import serializers

from MailService.models import AccountHolder, TransactionsDetails, Recommendations


class AccountHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountHolder
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionsDetails
        fields = '__all__'


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = '__all__'

