from django.urls import path
from . views import firstapi,registraionAPI,ContactapiView
urlpatterns = [
    path('firstapi/',firstapi),
    path('registration/',registraionAPI),
    path('contactapi/',ContactapiView.as_view()),
]
