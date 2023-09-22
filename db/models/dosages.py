import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Dosage(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    drug: str = Field(...)
    unit: str = Field(...)
    amount: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "drug": "B12",
                "unit": "IU",
                "amount": "2000"
            }
        }

    