from pydantic import BaseModel, ConfigDict
from pydantic import NonNegativeFloat, NonNegativeInt


class CatSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    year: NonNegativeInt
    breed: str
    salary: NonNegativeInt

class UpdateCat(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    salary: NonNegativeInt

class CatIdSchema(BaseModel):

    id: NonNegativeInt
  
    
