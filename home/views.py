from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.models import Member
from . serializers import MemberSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

class member_list(APIView):
    def get(self,request):
        member_one = Member.objects.all()
        serializer = MemberSerializer(member_one , many = True)
        return Response(serializer.data)

class create_member(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class update_member(UpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class delete_member(DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer