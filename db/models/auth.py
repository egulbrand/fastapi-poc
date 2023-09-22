from typing import Optional
from pydantic import BaseModel, Field

class OAuth2CredentialsRequestForm(BaseModel):
    grant_type: str = Field(...)
    username: Optional[str] = Field(...)
    password: Optional[str] = Field(...)
    client_id: Optional[str] = Field(...)
    client_secret: Optional[str] = Field(...)
