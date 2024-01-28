from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
	return 'so secret mmmmm'


