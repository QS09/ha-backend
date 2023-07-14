from django.contrib.auth import get_user_model
from rest_framework import views, status, viewsets

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema
from .serializers import RegisterSerializer, RefreshSerializer, UserSerializer


AuthUser = get_user_model()


@extend_schema(
        tags=["Auth"]
    )
class RegisterView(views.APIView):
    authentication_classes = []
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
        tags=["Auth"]
    )
class LoginView(TokenObtainPairView):
    pass


@extend_schema(
        tags=["Auth"]
    )
class LogoutView(views.APIView):
    authentication_classes = (JWTAuthentication,)
    serializer_class = RefreshSerializer

    def post(self, request, *args, **kwargs):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response(
                {"detail": "Successfully logged out."},
                status=status.HTTP_200_OK
            )
        except TokenError:
            return Response(
                {"detail": "Invalid refresh token."},
                status=status.HTTP_400_BAD_REQUEST
            )


@extend_schema(
        tags=["Auth"]
    )
class RefreshView(TokenRefreshView):
    pass


@extend_schema(
        tags=["Profile"]
    )
class ProfileView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
        tags=["User"]
    )
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = AuthUser.objects.all()
