import jwt
from ninja import NinjaAPI
from ninja.security import HttpBearer
from server.settings import SECRET_KEY

api = NinjaAPI(csrf=True)

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            #JWT secret key is set up in settings.py
            JWT_SIGNING_KEY = getattr(settings, "JWT_SIGNING_KEY", None)
            payload = jwt.decode(token, JWT_SIGNING_KEY, algorithms=["HS256"])
            username: str = payload.get("sub")
            if username is None:
                return None
        except jwt.PyJWTError as e:
            return None

        return username

@api.post("/token", auth=None)  # < overriding global auth
def get_token(request, username, password):
    if username == "admin" and password == "giraffethinnknslong":
        return {"token": "supersecret"}

'''
https://django-ninja.rest-framework.com/guides/authentication/
'''