from django.urls import path
from . views import firstapi

urlpatterns = [
    path('firstapi/',firstapi),
]
