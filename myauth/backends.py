import  jwt
from rest_framework import authentication


class JwtAuthentication(authentication.BaseAuthentication):

  def authenticate(self,request):
    return super().authenticate(request)