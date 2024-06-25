from django.urls import path
from .views import *


urlpatterns = [
    path('add/', add, name='add'),
    path('show/', show, name='showurl'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]

