
from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional

from ..cat.schemas import CatSchema


class TargetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name:str
    country:str
    notes:Optional[str] = None
    complete:bool = Field(default=False)



class MissionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    cat: Optional[CatSchema] = None
    targets: List[TargetSchema]
    complete: bool


class NoteSchema(BaseModel):

    text: str


