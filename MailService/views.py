from rest_framework import status, mixins, generics, viewsets, response, serializers
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
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RecommendationViewSet(viewsets.ViewSet):
    queryset = Recommendations.objects.all()

    def list(self, request):
        serializer = RecommendationSerializer(self.queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = RecommendationSerializer(data=request.data)
        if Recommendations.objects.filter(**request.data).exists():
            raise serializers.ValidationError("This data already exists")
        if serializer.is_valid():
            serializer.save()
            return response.Response(
                {"data": serializer.data}, status=status.HTTP_200_OK
            )
        return response.Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        serializer = RecommendationSerializer(data=request.data)
        try:
            data = Recommendations.objects.get(pk=pk)
            serializer.is_valid(raise_exception=True)
            serializer.update(data, serializer.data)
            return response.Response(
                {"data": serializer.data}, status=status.HTTP_200_OK
            )
        except Recommendations.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            serializer = Recommendations.objects.get(pk=pk)
            serializer.delete()
            return response.Response(
                {"message": "deleted successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        except Recommendations.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
