from django.urls import path
from .views import KlassAPIView, MehmonxonaAPIView, TravelAPIView

app_name = 'travel'

urlpatterns = [
    path('api/v1/klass/', KlassAPIView.as_view(), name='klass'),
    path('api/v1/mehmonxona/', MehmonxonaAPIView.as_view(), name='mehmonxona'),
    path('api/v1/travel/', TravelAPIView.as_view(), name='travel'),

    path('api/v1/klass/<int:pk>/', KlassAPIView.as_view(), name='klass'),
    path('api/v1/mehmonxona/<int:pk>/', MehmonxonaAPIView.as_view(), name='mehmonxona'),
    path('api/v1/travel/<int:pk>/', TravelAPIView.as_view(), name='travel'),

]