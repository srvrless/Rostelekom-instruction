

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
