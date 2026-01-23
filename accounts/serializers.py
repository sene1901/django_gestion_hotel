# # accounts/serializers.py
# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import smart_bytes, smart_str
# from django.core.mail import send_mail
# from django.conf import settings

# User = get_user_model()

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, min_length=6)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email'),
#             password=validated_data['password']
#         )
#         return user


# class ProfileImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("imageprofil",)  







# class EmailLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         email = data.get("email")
#         password = data.get("password")

#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             raise serializers.ValidationError("Email ou mot de passe incorrect")

#         user = authenticate(username=user.username, password=password)

#         if not user:
#             raise serializers.ValidationError("Email ou mot de passe incorrect")

#         return user





# # mot de passe oublier
# class PasswordResetRequestSerializer(serializers.Serializer):
#     email = serializers.EmailField()

#     def validate(self, attrs):
#         email = attrs.get('email')
#         if not User.objects.filter(email=email).exists():
#             raise serializers.ValidationError("Aucun utilisateur avec cet email")
#         return attrs

#     def save(self):
#         user = User.objects.get(email=self.validated_data['email'])
#         uid = urlsafe_base64_encode(smart_bytes(user.id))
#         token = PasswordResetTokenGenerator().make_token(user)

#         reset_link = f"http://localhost:5173/reset-password/{uid}/{token}"

#         send_mail(
#             subject="Réinitialisation de mot de passe",
#             message=f"Cliquez ici pour réinitialiser votre mot de passe : {reset_link}",
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[user.email],
#         )


# # nouveau mot de passe
# class SetNewPasswordSerializer(serializers.Serializer):
#     password = serializers.CharField(min_length=6)
#     token = serializers.CharField()
#     uidb64 = serializers.CharField()

#     def validate(self, attrs):
#         try:
#             user_id = smart_str(urlsafe_base64_decode(attrs['uidb64']))
#             user = User.objects.get(id=user_id)

#             if not PasswordResetTokenGenerator().check_token(user, attrs['token']):
#                 raise serializers.ValidationError("Token invalide ou expiré")

#             user.set_password(attrs['password'])
#             user.save()
#             return user

#         except Exception:
#             raise serializers.ValidationError("Lien invalide")

# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_bytes, smart_str
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()


# =========================
# REGISTER
# =========================
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user


# =========================
# PROFILE IMAGE
# =========================
class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("imageprofil",)


# =========================
# LOGIN EMAIL + PASSWORD
# =========================
class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email").lower()
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Email ou mot de passe incorrect")

        user = authenticate(
            username=user.username,
            password=password
        )

        if not user:
            raise serializers.ValidationError("Email ou mot de passe incorrect")

        return user


# =========================
# PASSWORD RESET REQUEST
# =========================
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get("email").lower()
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Aucun utilisateur avec cet email")
        return attrs

    def save(self):
        user = User.objects.get(email=self.validated_data["email"])
        uid = urlsafe_base64_encode(smart_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)

        reset_link = f"http://localhost:5173/reset-password/{uid}/{token}"

        send_mail(
            subject="Réinitialisation de mot de passe",
            message=f"Cliquez ici pour réinitialiser votre mot de passe : {reset_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )


# =========================
# SET NEW PASSWORD
# =========================
class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6)
    token = serializers.CharField()
    uidb64 = serializers.CharField()

    def validate(self, attrs):
        try:
            user_id = smart_str(urlsafe_base64_decode(attrs["uidb64"]))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(
                user, attrs["token"]
            ):
                raise serializers.ValidationError("Token invalide ou expiré")

            user.set_password(attrs["password"])
            user.save()

            return user

        except Exception:
            raise serializers.ValidationError("Lien invalide ou expiré")
