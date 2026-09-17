from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profileapi import views

router = DefaultRouter()
router.register('help-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profiles', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
