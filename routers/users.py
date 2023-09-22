from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends, Security
from fastapi.security import APIKeyHeader
from fastapi.encoders import jsonable_encoder
from db.models.users import UserBase, UserDisplay, UserUpdatePasword, UserSignUp
from db.ops.users import getAllUsers, getUser
from helpers.hashing import Hash
from typing import List
from auth.oauth2 import get_current_user


auth_header1 = APIKeyHeader(name="Authorization", scheme_name="token_header")
auth_header_client_id = APIKeyHeader(name="client_id", scheme_name="client_id_header")
auth_header_client_secret = APIKeyHeader(name="client_secret", scheme_name="client_secret_header")

router = APIRouter()

@router.get("/", response_description="Retrieve all users", status_code=status.HTTP_200_OK, response_model=List[UserDisplay])
def users(request: Request, auth_header_client_id=Security(auth_header_client_id), auth_header_client_secret=Security(auth_header_client_secret)):
    users = getAllUsers()
    return users

@router.get("/{id}", response_description="Retrieve user", status_code=status.HTTP_200_OK, response_model=UserDisplay)
def user(request: Request, id: str, current_user=Depends(get_current_user)):
    user = getUser(id)
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/signup", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=UserDisplay)
def create_user(request: Request, user: UserSignUp = Body(...)):
    try:
        user.password = Hash.brcypt(user.password)
        user = jsonable_encoder(user)
        new_user = request.app.database["users"].insert_one(user)
        created_user = request.app.database["users"].find_one(
            {"_id": new_user.inserted_id}
        )
        return created_user
    except Exception as e:
        print(e)

@router.post("/changepassword", response_description="Update a user's password", status_code=status.HTTP_201_CREATED, response_model=UserDisplay)
def create_user(request: Request, user: UserUpdatePasword = Body(...)):
    try:
        user = jsonable_encoder(user)
        new_user = request.app.database["users"].insert_one(user)
        created_user = request.app.database["users"].find_one(
            {"_id": new_user.inserted_id}
        )
        return created_user
    except Exception as e:
        print(e)

@router.patch("/", response_description="Update an existing user", status_code=status.HTTP_201_CREATED, response_model=UserDisplay)
def update_dosage(request: Request, user: UserDisplay = Body(...)):
    try:
        user = jsonable_encoder(user)
        new_user = request.app.database["users"].insert_one(user)
        created_user = request.app.database["users"].find_one(
            {"_id": new_user.inserted_id}
        )
        return created_user
    except Exception as e:
        print(e)


@router.delete("/", response_description="Delete an existing user", status_code=status.HTTP_200_OK)
def delete_dosage(request: Request, user: UserDisplay = Body(...)):
    try:
        users_query = {"_id": user.id}
        request.app.database["users"].delete_one(users_query)
        return
    except Exception as e:
        print(e)
