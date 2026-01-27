from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer


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
def hotel_create(request):
    serializer = HotelSerializer(
        data=request.data, context={'request': request}
    )
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def hotel_update(request, id):
    hotel = Hotel.objects.get(id=id, owner=request.user)
    serializer = HotelSerializer(
        hotel, data=request.data, partial=True, context={'request': request}
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def hotel_delete(request, id):
    hotel = Hotel.objects.get(id=id, owner=request.user)
    hotel.delete()
    return Response(
        {'message': 'Hôtel supprimé'},
        status=status.HTTP_204_NO_CONTENT
    )
