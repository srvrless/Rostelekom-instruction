from db.database import get_database
from fastapi import APIRouter, Depends, HTTPException
from dto.schemas import Item

from service.crud import (
    _create_instruction,
    _get_instruction,
    _create_header_instruction,
    _create_subitem,
)


router = APIRouter()


@router.get("/instructions")
async def get_instruction(db=Depends(get_database)):
    try:
        return await _get_instruction(db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/create_instance_instruction")
async def create_instruction(collection_name: str, db=Depends(get_database)):
    try:
        return await _create_instruction(collection_name, db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/create_header_instruction")
async def create_header_instruction(
    collection_name: str, item: Item, db=Depends(get_database)
):
    try:
        return await _create_header_instruction(collection_name, item, db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/create_subheader_instruction/{collection_name}")
async def create_subheader_instruction(
    collection_name: str, item: Item, db=Depends(get_database)
):
    try:
        return await _create_subitem(collection_name, item, db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


from db.database import get_database
from fastapi import APIRouter, Depends, HTTPException
from dto.schemas import Item

from service.crud import (
    _create_instruction,
    _get_instruction,
    _create_header_instruction,
    _create_subitem,
    _get_headers_instruction,
)


router = APIRouter()


@router.get("/instructions")
async def get_instruction(db=Depends(get_database)):
    try:
        return await _get_instruction(db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.get("/headears")
async def get_headers(db=Depends(get_database)):
    try:
        return await _get_headers_instruction(db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/create_instance_instruction")
async def create_instruction(collection_name: str, db=Depends(get_database)):
    try:
        return await _create_instruction(collection_name, db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/create_header_instruction")
async def create_header_instruction(
    collection_name: str, item: Item, db=Depends(get_database)
):
    try:
        return await _create_header_instruction(collection_name, item, db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/create_subheader_instruction/{collection_name}")
async def create_subheader_instruction(
    collection_name: str, item: Item, db=Depends(get_database)
):
    try:
        return await _create_subitem(collection_name, item, db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")
