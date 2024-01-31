from django.urls import path
from .views import *


urlpatterns = [
    path('', masterindex, name='masterindex'),
]
