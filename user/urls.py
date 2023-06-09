
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserView,UserCreateView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls'))
]
router = DefaultRouter()
router.register('create',UserCreateView)
router.register('',UserView)
urlpatterns += router.urls





