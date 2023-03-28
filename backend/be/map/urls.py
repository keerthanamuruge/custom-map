from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MapLocationView

router = DefaultRouter()
router.register('article', MapLocationView, basename='article')

urlpatterns = [
    path('viewset/', views.MapLocationView.as_view()),
    path('viewset/<int:pk>', views.MapLocationView.as_view()),
    path('', views.index, name='index'),
]