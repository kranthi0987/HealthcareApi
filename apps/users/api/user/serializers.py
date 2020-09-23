#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:14:00 2019

@author: sambhav
"""
import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from apps.users.api.profile.models import UserProfile
from apps.users.api.user.models import User

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'first_name', 'last_name', 'id', 'date_of_birth', 'phone_number', 'gender', 'camera_ip_address', 'wsport',
            'last_login_date_time', 'pic', 'address')


class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = self.initial_data['profile']
        json1_data = json.loads(profile_data)
        pic = self.initial_data['pic']
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            first_name=json1_data['first_name'],
            last_name=json1_data['last_name'],
            phone_number=json1_data['phone_number'],
            date_of_birth=json1_data['date_of_birth'],
            gender=json1_data['gender'],
            address=json1_data['address'],
            pic=pic
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }
