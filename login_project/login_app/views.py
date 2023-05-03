from django.shortcuts import render

# Create your views here.

from urllib import response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
# from login_api.serializers import UserSerializer, LoginSerializer
from login_app.models import User
import jwt, datetime
from rest_framework import status
from rest_framework.response import Response


# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication

class Login_View(APIView):
    # permission_classes = (IsAuthenticated, )
    # authentication_classes = [JWTAuthentication]
    def post(self, request):
        var_email = request.data['email']
        var_password = request.data['password']

        var_user = User.objects.filter(email=var_email).first()

        if var_user is None:
            raise AuthenticationFailed('User not found!')

        if not var_user.check_password(var_password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {

            'id': var_user.id,
            'email': var_user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()

        }

        var_token = jwt.encode(payload, 'secret', algorithm='HS256').encode().decode('utf-8')

        return Response({
            'jwt': var_token,
            'id': var_user.id
        })
