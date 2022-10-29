from django.urls import path
from MailService import views
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r"AccountDetails", views.AccountMixin)


urlpatterns = [
    path("account/", views.AccountMixin.as_view(), name="accounts_gp"),
    path("account/<int:pk>", views.AccountMixin.as_view(), name="accounts_pd")
]

