from db.database import get_database
from fastapi import APIRouter, Depends, HTTPException

from crud.instruction import _create_instruction, _get_instruction


router = APIRouter()


@router.get("/instructions")
async def get_instruction(db=Depends(get_database)):
    try:
        return await _get_instruction(db)
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {error}")


@router.post("/create_instance_instruction")
async def create_instruction(collection_name: str, db=Depends(get_database)):
    try:
        return await _create_instruction(collection_name, db)
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {error}")
