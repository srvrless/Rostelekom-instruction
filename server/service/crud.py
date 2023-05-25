from dto.schemas import Item
from dto.schemas import SubItem


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
        
    except Exception as error:
        return f"DatabaseException: {error}"


async def _create_header_instruction(collection: str, item: Item, session):
    item_data = {
        "title": item.title,
        "text": item.text,
        "image": item.image,
        "sub_items": [],
    }
    result = session[collection].insert_one(item_data)
    return {"message": "Item created successfully", "item_id": str(result.inserted_id)}


async def _create_subitem(collection: str, subitem: Item, session):
    parent_item = session[collection].find_one({"title": subitem.title})
    if not parent_item:
        return {"message": "Parent item not found"}

    # Создать подзапись на основе родительской записи
    subitem_data = {
        "title": subitem.title,
        "text": subitem.text,
        "image": subitem.image,
        "sub_items": [],
    }

    result = session[collection].update_one(
        {"_id": parent_item["_id"]}, {"$push": {"sub_items": subitem_data}}
    )

    if result.modified_count == 1:
        return {"message": "Subitem created successfully"}
    else:
        return {"message": "Failed to create subitem"}
