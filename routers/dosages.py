from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from db.models.dosages import Dosage
from typing import List

router = APIRouter()

@router.get("/", response_description="Retrieve all dosages", status_code=status.HTTP_200_OK, response_model=List[Dosage])
def dosages(request: Request):
    dosages = request.app.database["dosages"].find()
    return dosages

@router.get("/{id}", response_description="Retrieve all dosages", status_code=status.HTTP_200_OK, response_model=Dosage)
def dosages(request: Request, id):
    dosage = None
    dosage_query = {"_id": id}
    dosage = request.app.database["dosages"].find_one(dosage_query)
    if dosage == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dosage not found")
    return dosage

@router.post("/", response_description="Create a new dosage", status_code=status.HTTP_201_CREATED, response_model=Dosage)
@router.post("/current", response_description="Create a new dosage", status_code=status.HTTP_201_CREATED, response_model=Dosage)
@router.post("/v_0_1_0", response_description="Create a new dosage", status_code=status.HTTP_201_CREATED, response_model=Dosage)
def create_dosage(request: Request, dosage: Dosage = Body(...)):
    try:
        dosage = jsonable_encoder(dosage)
        new_dosage = request.app.database["dosages"].insert_one(dosage)
        created_dosage = request.app.database["dosages"].find_one(
            {"_id": new_dosage.inserted_id}
        )
        return created_dosage
    except Exception as e:
        print(e)

@router.patch("/", response_description="Update an existing dosage", status_code=status.HTTP_201_CREATED, response_model=Dosage)
def update_dosage(request: Request, dosage: Dosage = Body(...)):
    try:
        dosage = jsonable_encoder(dosage)
        new_dosage = request.app.database["dosages"].insert_one(dosage)
        created_dosage = request.app.database["dosages"].find_one(
            {"_id": new_dosage.inserted_id}
        )
        return created_dosage
    except Exception as e:
        print(e)


@router.delete("/", response_description="Delete an existing dosage", status_code=status.HTTP_200_OK)
def delete_dosage(request: Request, dosage: Dosage = Body(...)):
    try:
        dosage_query = {"_id": dosage.id}
        print(str(dosage_query))
        request.app.database["dosages"].delete_one(dosage_query)
        return
    except Exception as e:
        print(e)
