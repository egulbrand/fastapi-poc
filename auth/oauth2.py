from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from db.ops.users import getUser
import os 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = os.environ['AUTH_SECRET_KEY']
 
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt
 
def get_current_user(token: str = Depends(oauth2_scheme)):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id: str = payload.get("sub")
    if user_id is None:
      raise credentials_exception
  except JWTError:
    raise credentials_exception
#   usersDBOps.setApp(app)
  user = getUser(user_id)
  if user is None:
    raise credentials_exception
  return user