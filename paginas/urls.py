from django.urls import path
from .views import IndexView, AdminView

urlpatterns = [
    path('', IndexView.as_view(), name='login'),
    path('admin/', AdminView.as_view(), name='admin'),
]