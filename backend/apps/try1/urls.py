from django.urls import path
from . import views

urlpatterns = [
    path('', views.TryList.as_view(), name='Try_list'),
]