# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Activity,User
from .serializers import UserSerializer,ActivitySerializer
class ActivityView(APIView):

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response({"ok": True, "members": serializer.data})

