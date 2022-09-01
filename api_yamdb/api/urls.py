from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoriesViewSet,
                    CommentViewSet,
                    GenreViewSet,
                    ReviewViewSet,
                    TitlesViewSet,)


router = DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'categories', CategoriesViewSet, basename='categories'),
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitlesViewSet, basename='titles')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                r'/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('', include('user.urls'))
    # path('v1/auth/token/', get_token, name='token'),
    # path('v1/auth/signup/', get_confirmation_code, name='get_code'),
]
