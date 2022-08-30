from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet,
                    get_confirmation_code,
                    get_token)

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', get_token, name='token'),
    path('v1/auth/signup/', get_confirmation_code, name='get_code')
]