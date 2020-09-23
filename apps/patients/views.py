from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.patients.models import PatientModel, PatientLogModel
from apps.patients.serializers import PatientSerializer, PatientLogSerializer


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def patients_list(request):
    """
    List all products, or create a new product.
    """
    # permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication
    # Getting the list of patients or create Patient
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def patient_list_byid(request):
    """
    List all products by Doc id.
    """
    # permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication
    # Getting the list of patients or create Patient
    if request.method == 'POST':
        # products = PatientModel.objects.all()
        products = PatientModel.objects.filter(doc_id=request.data['doc_id'])
        serializer = PatientSerializer(products, context={'request': request}, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def patient_count(request):
    """
    List all products, or create a new product.
    """
    # permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication
    # Getting the list of patients or create Patient
    if request.method == 'POST':
        products = PatientModel.objects.filter(doc_id=request.data['doc_id']).count()
        return Response(products)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def patient_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """
    # permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication

    try:
        product = PatientModel.objects.get(pk=pk)
    except PatientModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(product, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def patientslog_list_byid(request):
    """
    List all products, or create a new product.
    """
    # permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication

    if request.method == 'POST':
        patientslog_list = PatientLogModel.objects.filter(patient_id=request.data['patient_id']).all()
        serializer = PatientLogSerializer(patientslog_list, context={'request': request}, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def patientslog_post_byid(request):
    """
    List all products, or create a new product.
    """
    # permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication
    if request.method == 'POST':
        serializer = PatientLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def patientslog_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """
    # permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication

    try:
        patientslog_list = PatientLogModel.objects.get(pk=pk)
    except PatientLogModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientLogSerializer(patientslog_list, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientLogSerializer(patientslog_list, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patientslog_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
