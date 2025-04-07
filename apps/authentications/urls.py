from django.urls import path

from apps.authentications.views import LoginView

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
]
