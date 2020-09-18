#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import status, viewsets, parsers, response, decorators
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.api.profile.models import UserProfile
from apps.users.api.user.serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.parsers import FormParser, MultiPartParser


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User registered  successfully',
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
