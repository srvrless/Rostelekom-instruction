from typing import Union
from db.database import get_database
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from dto.schemas import Item

from service.crud import (
    _upload_image,
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


@router.get("/header_instruction/{collection_name}")
async def get_instruction(collection_name, db=Depends(get_database)):
    try:
        return await _get_headers_instruction(collection_name, db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/create_instance_instruction")
async def create_instruction(collection_name: str, db=Depends(get_database)):
    try:
        return await _create_instruction(collection_name, db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/create_header_instruction/{collection_name}/")
async def create_header_instruction(
    collection_name: str,
    title: str,
    text: str,
    image: Union[UploadFile, None] = File(...),
    db=Depends(get_database),
):
    try:
        return await _create_header_instruction(collection_name, title, text, image, db)
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/create_subheader_instruction/{collection_name}/{search_title}")
async def create_subheader_instruction(
    collection_name: str,
    search_title: str,
    title: str,
    text: str,
    image: Union[UploadFile, None] = File(...),
    db=Depends(get_database),
):
    try:
        return await _create_subitem(
            collection_name, search_title, title, text, image, db
        )
    except Exception as error:
        raise HTTPException(status_code=403, detail=f"Something went wrong: {error}")


@router.post("/upload/file")
async def upload_file(image: UploadFile = File(...)):
    return await _upload_image(image)
