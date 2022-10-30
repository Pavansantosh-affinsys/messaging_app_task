from django.urls import path, include
from MailService import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"recommendation", views.RecommendationViewSet)


urlpatterns = [
    path("account/", views.AccountMixin.as_view(), name="accounts_gp"),
    path("account/<int:pk>", views.AccountMixin.as_view(), name="accounts_pd"),
    path("transaction/", views.TransactionMixin.as_view(), name="transaction_gp"),
    path("", include(router.urls)),
]
