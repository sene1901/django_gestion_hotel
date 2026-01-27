
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    RegisterSerializer,
    PasswordResetRequestSerializer,
    SetNewPasswordSerializer,
    EmailLoginSerializer,
    ProfileImageSerializer,
)

import traceback 
User = get_user_model()


# =========================
# REGISTER
# =========================
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        try:
            print("=" * 60)
            print("🔍 REGISTER - DÉBUT")
            print(f"Données reçues: {request.data}")
            print("=" * 60)
            
            serializer = self.get_serializer(data=request.data)
            
            if serializer.is_valid():
                print("✓ Données valides")
                user = serializer.save()
                print(f"✓ Utilisateur créé: {user.username}")
                
                headers = self.get_success_headers(serializer.data)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                    headers=headers
                )
            else:
                print(f"✗ Erreurs de validation: {serializer.errors}")
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        except Exception as e:
            print("=" * 60)
            print("❌ ERREUR CRITIQUE:")
            print(f"Type: {type(e).__name__}")
            print(f"Message: {str(e)}")
            print(f"Traceback:")
            traceback.print_exc()
            print("=" * 60)
            
            return Response(
                {
                    "error": str(e),
                    "type": type(e).__name__,
                    "traceback": traceback.format_exc()
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# =========================
# LOGIN EMAIL + PASSWORD
# =========================
class EmailLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            print("🔍 LOGIN - DÉBUT")
            print(f"Données reçues: {request.data}")
            
            serializer = EmailLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "username": user.username,
                    },
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print(f"❌ ERREUR LOGIN: {e}")
            traceback.print_exc()
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


# =========================
# PROFILE (user connecté)
# =========================
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "imageprofil": user.imageprofil.url if getattr(user, "imageprofil", None) else None,
            }
        )


# =========================
# UPDATE PROFILE IMAGE
# =========================
class ProfileImageUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request):
        user = request.user
        serializer = ProfileImageSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Photo de profil mise à jour",
                "imageprofil": serializer.data.get("imageprofil"),
            },
            status=status.HTTP_200_OK,
        )


# =========================
# PASSWORD RESET REQUEST
# =========================
class PasswordResetRequestView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as e:
            # Si l'envoi du mail échoue
            return Response(
                {"error": "Impossible d'envoyer l'email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({"message": "Email envoyé"}, status=status.HTTP_200_OK)


# =========================
# SET NEW PASSWORD
# =========================
class SetNewPasswordView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Mot de passe réinitialisé"}, status=status.HTTP_200_OK)


# =========================
# LOGOUT
# =========================
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Token manquant"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Token invalide ou expiré"}, status=status.HTTP_400_BAD_REQUEST)
