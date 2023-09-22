from fastapi import APIRouter, Request, Depends, HTTPException, status, Form
from typing import Optional, Annotated
from pydantic import BaseModel, Field
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from db.ops.users import getUserByUserName
from db.models.users import UserBase
from helpers.hashing import Hash
from auth.oauth2 import create_access_token
from db.models.auth import OAuth2CredentialsRequestForm

router= APIRouter()

@router.post('/login')
def login(request: Request, credentialsForm: OAuth2PasswordRequestForm = Depends()):
    print(credentialsForm.grant_type)
    user = getUserByUserName(credentialsForm.client_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(user['password'], credentialsForm.client_secret):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    access_token = create_access_token(data={
        'sub': user['_id'],
        'username': user['username'],
        'firstname': user['firstname'],
        'lastName': user['lastname']
        })
    
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user['_id'],
        'username': user['username']
    }

@router.post('/authenticate')
def login(request: Request, grant_type: Annotated[str, Form()], client_id: Annotated[str, Form()], client_secret: Annotated[str, Form()]):
    print(grant_type)
    user = getUserByUserName(client_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(user['password'], client_secret):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    access_token = create_access_token(data={
        'sub': user['_id'],
        'username': user['username'],
        'firstname': user['firstname'],
        'lastName': user['lastname']
        })
    
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user['_id'],
        'username': user['username']
    }