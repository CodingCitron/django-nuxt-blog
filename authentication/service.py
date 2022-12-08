import jwt

def create_token(username):
    JWT_SIGNING_KEY = getattr(settings, "JWT_SIGNING_KEY", None)
    JWT_ACCESS_EXPIRY = getattr(settings, "JWT_ACCESS_EXPIRY", "15") # 15 minutes expiration
    to_encode_access = {"sub": username}
    access_expire = datetime.utcnow() + timedelta(minutes=JWT_ACCESS_EXPIRY)
    to_encode_access.update({"exp": access_expire})
    encoded_access_jwt = jwt.encode(to_encode_access, JWT_SIGNING_KEY, algorithm="HS256")
    return encoded_access_jwt