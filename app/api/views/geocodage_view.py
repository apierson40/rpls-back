from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services import GeocodageService


@api_view(['GET'])
def run_geocodage(request):
    if request.method == 'GET':
        geocodage_service = GeocodageService()
        geocodage_service.geocode_csv_data()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
