from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SystemStatus
from .serializers import SystemStatusSerializer

def home(request):
    return render(request, 'home/home.html')

def tuna(request):
    return render(request, 'home/tuna.html')

def coral(request):
    return render(request, 'home/coral.html')

def tbd(request):
    return render(request, 'home/tbd.html')

class SystemStatusAPI(APIView):
    def get(self, request):
        swarm_states = ["OPERATIONAL", "DEGRADED", "OFFLINE"]
        data = {
            "swarm_state": random.choice(swarm_states),
            "active_nodes": random.randint(3, 18),
            "last_updated": timezone.now().isoformat(),
        }
        return Response(data)
