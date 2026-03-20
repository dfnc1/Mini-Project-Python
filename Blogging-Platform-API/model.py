from typing import List
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    category: str
    tags: List[str]
