from django.urls import path
from .views import RequestController

app_name = 'api'

urlpatterns = [
    path('', RequestController.as_view()),
]
