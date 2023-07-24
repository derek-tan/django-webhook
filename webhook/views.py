from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import process_agreement_changes


def index(request):
    return HttpResponse("You are at webhook landing page")

@api_view(['POST'])
def subscribe_soda_agreement(request):
    print("Receiving soda agreement changes event")
    process_agreement_changes.delay()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def subscribe_soda_notification(request):
    # TODO: handle alert notification
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def subscribe_soda_incident(request):
    # TODO: handle incident
    return Response(status=status.HTTP_200_OK)
