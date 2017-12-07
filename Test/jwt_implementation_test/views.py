from django.shortcuts import render
from django.views import View
from .models import *
from rest_framework import viewsets
from .serializers import *
import jwt
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


class BankRegisterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BankRegisters to be viewed and edited
    """
    queryset = BankRegister.objects.all()
    serializer_class = BankRegisterSerializer


@staff_member_required
def test_view(request):
    if request.method == "GET":
        return render(request, "test.html")


