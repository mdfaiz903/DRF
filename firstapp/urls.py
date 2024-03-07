from django.urls import path
from . views import firstapi,registraionAPI,ContactapiView,PostCreateApiView,PostRetriveAPIVIEW
urlpatterns = [
    path('firstapi/',firstapi),
    path('registration/',registraionAPI),
    path('contactapi/',ContactapiView.as_view()),
    path('post/',PostCreateApiView.as_view()),
    # path('postlist/',PostListApiView.as_view()),
    path('postretrive/<int:id>/',PostRetriveAPIVIEW.as_view()),
]
