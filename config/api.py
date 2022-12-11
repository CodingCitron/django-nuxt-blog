from ninja import NinjaAPI
from account.service import GlobalAuth
from account.api import router as auth_router

api = NinjaAPI(auth=GlobalAuth())

api.add_router("/auth/", auth_router)

