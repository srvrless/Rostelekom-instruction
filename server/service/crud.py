from time import strftime
from fastapi import HTTPException, UploadFile

async def _create_instruction(collection_name: str, session):
    try:
        if collection_name not in session.list_collection_names():
            session.create_collection(collection_name)
        return collection_name
    except Exception as error:
        return f"DatabaseException: {error}"


async def _get_instruction(session):
    try:
        collections = session.list_collection_names()
        return collections
    except Exception as error:
        return f"DatabaseException: {error}"


async def _get_headers_instruction(collection_name, session):
    try:
        collection = session[collection_name]
        items = collection.find()
        data = []
        for item in items:
            data.append(item)
        return data
    except Exception as error:
        return f"DatabaseException: {error}"


async def _create_header_instruction(
    collection: str, title: str, text: str, image: UploadFile, session
):
    path_to_file = await _upload_image(image)
    item_data = {
        "title": title,
        "text": text,
        "image": path_to_file,
        "sub_items": [],
    }
    result = session[collection].insert_one(item_data)
    return {"message": "Item created successfully", "item_id": str(result.inserted_id)}


async def _create_subitem(
    collection: str, search_title, title: str, text: str, image: UploadFile, session
):
    parent_item = session[collection].find_one({"title": search_title})
    if not parent_item:
        return {"message": "Parent item not found"}

    # Создать подзапись на основе родительской записи
    path_to_file = await _upload_image(image)
    subitem_data = {
        "title": title,
        "text": text,
        "image": path_to_file,
        "sub_items": [],
    }

    result = session[collection].update_one(
        {"_id": parent_item["_id"]}, {"$push": {"sub_items": subitem_data}}
    )

    if result.modified_count == 1:
        return {"message": "Subitem created successfully"}
    else:
        return {"message": "Failed to create subitem"}


async def _upload_image(image: UploadFile):
    def is_image(filename: str) -> bool:
        valid_extensions = (".png", ".jpg", ".jpeg", "gif")
        return filename.endswith(valid_extensions)

    def upload_image():
        """Upload image with add datetime on root directory"""
        if is_image(image.filename):
            timestr = strftime("%Y%m%d-%H%M%S")
            image_name = timestr + image.filename

            with open(f"static/images/{image_name}", "wb+") as image_file_upload:
                image_file_upload.write(image.file.read())
            return f"static/images/{image_name}"

        raise HTTPException(status_code=404, detail=f"Image not found")

    return upload_image()
