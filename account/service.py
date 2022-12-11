import jwt
from datetime import datetime, timedelta
from django.conf import settings

from ninja.security import HttpBearer
from ninja.errors import ValidationError

access = ['username', '']

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        print(request)
        try:
            JWT_SIGNING_KEY = getattr(settings, 'JWT_SIGNING_KEY', None)
            payload = jwt.decode(token, JWT_SIGNING_KEY, algorithms=['HS256'])
            
            username: str = payload.get('name')

            if username is None:
                return None
        except jwt.PyJWTError as e:
            return None

        return username

def create_token(user = None, type = None):

    JWT_SIGNING_KEY = getattr(settings, 'JWT_SIGNING_KEY', None)

    if type != None: # access
        EXPIRY = getattr(settings, 'JWT_ACCESS_EXPIRY', 15) 
    else: # refresh
        EXPIRY = getattr(settings, 'JWT_REFRESH_EXPIRY', 240)

    to_encode_access = {}
    
    if user != None:
        for key in user:
            to_encode_access[key] = user[key]

    access_expire = datetime.utcnow() + timedelta(minutes = EXPIRY)

    to_encode_access.update({
        'exp': access_expire
    })

    encoded_access_jwt = jwt.encode(
        to_encode_access, 
        JWT_SIGNING_KEY, 
        algorithm='HS256'
    )
    
    return encoded_access_jwt

