from django.urls import path
from . views import firstapi,registraionAPI

urlpatterns = [
    path('firstapi/',firstapi),
    path('registration/',registraionAPI),
]
