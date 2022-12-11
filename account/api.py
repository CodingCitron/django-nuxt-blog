from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password, make_password
from ninja import Router, Schema
from ninja.security import HttpBearer
from .service import create_token
from django.http import HttpRequest, HttpResponse
from django.core.exceptions import SuspiciousOperation

router = Router()

class TokenSchema(Schema):
    access: str

class SignIn(Schema):
    username: str
    password: str

class SignUp(Schema):
    username: str
    password: str

class SignOut(Schema):
    pass

@router.post(
    '/sign-in',
    auth = None
)
def sign_in(request, payload: SignIn, response: HttpResponse):
    obj = payload.dict()
    
    try:
        user_model = get_user_model().objects.get(username=obj['username'])
    except get_user_model().DoesNotExist:
        raise ValidationError

    passwords_match = check_password(obj['password'], user_model.password)
    if not passwords_match:
        raise ValidationError
    
    access = create_token({ 'username': user_model.username }, 'access')
    refresh = create_token()

    response.set_cookie(
        key = 'refresh-token', 
        value = refresh
    # , httponly=True
    )

    return 200, TokenSchema(access = access)


@router.post(
    '/sign-up',
    auth = None,
)
def sign_up(request, payload: SignUp):
    obj = payload.dict()

    User = get_user_model()

    username = obj['username']
    password = obj['password']

    if User.objects.filter(username=username).exists():
        raise SuspiciousOperation('%s is duplicate username' % username)

    hashed_password = make_password(password)

    User.objects.create(
        username = username,
        password = hashed_password
    )
    # User.save()

    return 200, { 'message': 'SUCCESS' }

@router.post(
    '/sign-out'
)
def sign_out(request, payload:SignOut):
    pass

@router.post(
    '/refresh'
)
def refresh_token(request): 
    pass