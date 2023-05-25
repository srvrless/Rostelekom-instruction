from typing import List, Optional
from pydantic import BaseModel


class SubItem(BaseModel):
    title: str
    text: str
    image: Optional[str]


class Item(BaseModel):
    title: str
    text: str
    image: Optional[str]
    subitems: Optional[List[SubItem]]
