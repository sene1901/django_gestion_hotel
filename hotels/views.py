from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
import traceback


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hotel_list(request):
    hotels = Hotel.objects.filter(owner=request.user)
    serializer = HotelSerializer(
        hotels, many=True, context={'request': request}
    )
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def hotel_create(request):
    try:
        print("=" * 60)
        print("🔍 CRÉATION HÔTEL - DÉBUT")
        print(f"User: {request.user}")
        print(f"User authenticated: {request.user.is_authenticated}")
        print(f"Données reçues: {request.data}")
        print(f"Fichiers: {request.FILES}")
        print("=" * 60)
        
        # Créer une copie mutable des données
        data = request.data.copy()
        
        serializer = HotelSerializer(data=data, context={'request': request})
        
        if serializer.is_valid():
            print("✓ Données valides")
            hotel = serializer.save(owner=request.user)
            print(f"✓ Hôtel créé: {hotel.name}")  # ⚠️ CHANGÉ: nom → name
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(f"✗ Erreurs de validation: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        print("=" * 60)
        print("❌ ERREUR CRITIQUE:")
        print(f"Type: {type(e).__name__}")
        print(f"Message: {str(e)}")
        print("Traceback complet:")
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


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def hotel_update(request, id):
    try:
        print(f"🔍 UPDATE HÔTEL ID: {id}")
        hotel = Hotel.objects.get(id=id, owner=request.user)
        
        # Créer une copie mutable des données
        data = request.data.copy()
        
        serializer = HotelSerializer(
            hotel, 
            data=data, 
            partial=True, 
            context={'request': request}
        )
        
        if serializer.is_valid():
            serializer.save()
            print(f"✓ Hôtel mis à jour: {hotel.name}")  # ⚠️ CHANGÉ: nom → name
            return Response(serializer.data)
        else:
            print(f"✗ Erreurs: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    except Hotel.DoesNotExist:
        return Response(
            {"error": "Hôtel non trouvé"}, 
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        print(f"❌ ERREUR UPDATE: {e}")
        traceback.print_exc()
        return Response(
            {"error": str(e), "traceback": traceback.format_exc()}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def hotel_delete(request, id):
    try:
        hotel = get_object_or_404(Hotel, id=id, owner=request.user)
        name = hotel.name  # ⚠️ CHANGÉ: nom → name
        hotel.delete()
        print(f"✓ Hôtel supprimé: {name}")
        return Response(
            {'message': f'Hôtel "{name}" supprimé avec succès'},
            status=status.HTTP_204_NO_CONTENT
        )
    except Exception as e:
        print(f"❌ ERREUR DELETE: {e}")
        traceback.print_exc()
        return Response(
            {"error": str(e)}, 
            status=status.HTTP_400_BAD_REQUEST
        )