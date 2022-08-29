from dataclasses import fields
from xml.parsers.expat import model
from rest_framework import serializers
from home.models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'