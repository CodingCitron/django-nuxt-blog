from ninja import NinjaAPI
from ninja.security import HttpBearer
from account.api import router as auth_router
from ninja.errors import ValidationError

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token

api = NinjaAPI(auth=GlobalAuth())

api.add_router("/auth/", auth_router)

