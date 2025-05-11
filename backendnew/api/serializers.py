from .models import (
    student,
    teacher,
    course_category
    ,
    course,
    video,
    Common_user,
)

from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def validate_email(self, value):
        if student.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("Email already exists."))
        return value

    def validate_phone_number(self, value):
        if student.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(_("Phone number already exists."))
        return value
    
    
class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def validate_email(self, value):
        if teacher.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("Email already exists."))
        return value

    def validate_phone_number(self, value):
        if teacher.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(_("Phone number already exists."))
        return value

class course_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = course_category
        fields = '__all__'
        extra_kwargs = {
            'description': {'write_only': True}
        }

    def create(self, validated_data):
        return super().create(validated_data)
    

class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ['id', 'video']

class courseSerializer(serializers.ModelSerializer):
    videos = videoSerializer(many=True, read_only=True)

    class Meta:
        model = course
        fields = '__all__'
        extra_kwargs = {
            'description': {'write_only': True}
        }

    def create(self, validated_data):
        return super().create(validated_data)

class coursevideoserializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = '__all__'
    

        

class Common_user_serializers(serializers.ModelSerializer):
    class Meta:
        model = Common_user
        fields = '__all__'

    


