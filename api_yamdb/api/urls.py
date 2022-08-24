from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    ReviewViewSet
)


router = DefaultRouter()
router.register()
router.register(r'title/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'title/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                r'/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', views.obtain_auth_token, name='token'),
    path('v1/auth/signup', )
]
