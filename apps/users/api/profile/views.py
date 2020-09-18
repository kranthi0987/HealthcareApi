
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.users.api.profile.models import UserProfile


class UserProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status_code': status_code,
                'message': 'User profile fetched successfully',
                'first_name': user_profile.first_name,
                'last_name': user_profile.last_name,
                'phone_number': user_profile.phone_number,
                'date_of_birth': user_profile.date_of_birth,
                'gender': user_profile.gender,
                'id': user_profile.id,
                'email': request.user.email,
                'last_login_date_time': user_profile.last_login_date_time,
                'specialist': user_profile.specialist,
                'camera_ip_address': user_profile.camera_ip_address,
                'wsport': user_profile.wsport,
                'pic': user_profile.pic.url,
                'server_ip_address': user_profile.server_ip_address,

            }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
            }
        return Response(response, status=status_code)
