from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services import DataIntegrationService


@api_view(['GET'])
def run_data_integration(request):
    if request.method == 'GET':
        data_integration_service = DataIntegrationService()
        data_integration_service.integrate_geocoded_csv_data()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
