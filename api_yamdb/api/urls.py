from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register()

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', views.obtain_auth_token, name='token'),
    path('v1/auth/signup', )
]