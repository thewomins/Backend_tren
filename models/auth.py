from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from dotenv import dotenv_values

config = dotenv_values(".env")

class Hasher():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = config.get("SECRET")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def encode_token(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )
    
    def decode_token(self, token):
       try:
           #print("entro decode")
           payload = jwt.decode(token, self.secret, algorithms=['HS256'])
           #print(payload)
           return payload['sub']
       except jwt.ExpiredSignatureError:
           raise HTTPException(status_code=401, detail='Signature has expired')
       except jwt.InvalidTokenError as e:
           raise HTTPException(status_code=401, detail='Invalid token')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        #print(self.decode_token(auth.credentials))
        return self.decode_token(auth.credentials)