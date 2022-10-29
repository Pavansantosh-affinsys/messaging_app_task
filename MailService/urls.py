from django.urls import path
from MailService import views


urlpatterns = [
    path("account/", views.AccountMixin.as_view(), name="accounts_gp"),
    path("account/<int:pk>", views.AccountMixin.as_view(), name="accounts_pd"),
    path("transaction/", views.TransactionMixin.as_view(), name="transaction_gp"),
]
