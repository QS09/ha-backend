from django.urls import path
from rest_framework.routers import DefaultRouter
from api.Auth.views import LogoutView, LoginView, RegisterView, ProfileView, UserViewSet

urlpatterns = [
    # path("", include('djoser.urls'), name="djoser"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns += router.urls
