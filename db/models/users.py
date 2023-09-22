import uuid
from typing import Optional
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    email: str = Field(...)
    username: str = Field(...)
    firstname: str = Field(...)
    middlename: Optional[str] = Field(...)
    lastname: str = Field(...)
    password: str = Field(...)
    user_confirmed: bool = Field(...)

    class Config:
        from_attributes = True
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "email": "someone@somewhere.fake",
                "firstname": "Santa",
                "middlename": "",
                "lastname": "Clause",
                "password": "supersecure",
                "user_confirmed": False
            }
        }


class UserUpdatePasword(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    current_password: str = Field(...)
    new_password: str = Field(...)
    confirm_new_password: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "current_password": "supersecurecurrent",
                "new_password": "supersecurenew",
                "confirm_new_password": "supersecurenew",
            }
        }

class UserDisplay(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    email: str = Field(...)
    username: str = Field(...)
    firstname: str = Field(...)
    middlename: Optional[str] = Field(...)
    lastname: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "email": "someone@somewhere.fake",
                "firstname": "Santa",
                "middlename": "",
                "lastname": "Clause",
            }
        }


class UserSignUp(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    email: str = Field(...)
    username: str = Field(...)
    firstname: str = Field(...)
    middlename: Optional[str] = Field(...)
    lastname: str = Field(...),
    password: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "email": "someone@somewhere.fake",
                "username": "someone",
                "firstname": "Santa",
                "middlename": "",
                "lastname": "Clause",
                "password": "supersecure"
            }
        }
