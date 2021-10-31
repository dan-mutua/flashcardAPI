import  jwt
from rest_framework import authentication


class JwtAuthentication(authentication.BaseAuthentication):

  def authenticate(self,request):
    auth_data=authentication.get_authorization_header(request)

    if not auth_data:
      return None


    return super().authenticate(request)