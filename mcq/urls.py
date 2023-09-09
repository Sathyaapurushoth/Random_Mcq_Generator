from django.urls import path
from .views import Mcq, RandomQuestion, McqQuestion

app_name='Mcq'

urlpatterns = [
    path('', Mcq.as_view(), name='Mcq'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random' ),
    path('q/<str:topic>/', McqQuestion.as_view(), name='questions' ),
]
