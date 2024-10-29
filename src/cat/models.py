from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class Cat(Base):
    __tablename__ = "spyCats"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    year: Mapped[float]
    breed: Mapped[str]
    salary: Mapped[int]
    missions: Mapped[list["Mission"]] = relationship("Mission", back_populates="cat") 
