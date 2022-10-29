from django.shortcuts import render
from rest_framework import status, mixins, generics
from .models import AccountHolder, TransactionsDetails, Recommendations
from .serializer import (
    AccountHolderSerializer,
    TransactionSerializer,
    RecommendationSerializer,
)


class AccountMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):

    queryset = AccountHolder.objects.all()
    serializer_class = AccountHolderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TransactionMixin(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):

    queryset = TransactionsDetails.objects.all()
    serializer_class = TransactionsDetails

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
