from django.urls import path
from . views import firstapi,registraionAPI,ContactapiView,PostCreateApiView
urlpatterns = [
    path('firstapi/',firstapi),
    path('registration/',registraionAPI),
    path('contactapi/',ContactapiView.as_view()),
    path('post/',PostCreateApiView.as_view()),
]
