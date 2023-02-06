from django.urls import path
from .views import ReviewAPIView

app_name = 'api'

urlpatterns = [
    path('<int:id>/', ReviewAPIView.as_view(), name='review-detail')
]