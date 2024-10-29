from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Annotated


from .database import get_db

MAX_TARGET_PER_MISSION = 3


db_session = Annotated[Session, Depends(get_db)]