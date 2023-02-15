from typing import List, Dict, Optional, Literal
from pydantic import BaseModel


class File(BaseModel):
    type: Literal["board", "notebook", "file"]
    path: str
    active: Optional[bool] = False


class Template(BaseModel):
    name: str
    isOverview: bool
    description: str
    automaticArguments: Dict[str, str]
    userArguments: dict
    files: List[File]


class Category(BaseModel):
    name: str
    description: str
    templates: List[Template]
