from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ..database import Base
from ..cat.models import Cat

class Target(Base):
    __tablename__ = "targets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(255))
    notes: Mapped[str]
    complete: Mapped[bool] = mapped_column(Boolean, default=False)
    mission_id: Mapped[int] = mapped_column(ForeignKey("missions.id"))
    mission: Mapped['Mission'] = relationship('Mission', back_populates='targets')



class Mission(Base):
    __tablename__ = "missions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cat_id: Mapped[int] = mapped_column(ForeignKey("spyCats.id"), nullable=True)
    cat: Mapped["Cat"] = relationship(back_populates='missions')
    targets: Mapped[list[Target]] = relationship("Target", back_populates="mission", cascade="all, delete-orphan")
    complete:Mapped[bool] = mapped_column(Boolean, default=False)

    def check_and_complete_mission(self, db):
        if all(target.complete for target in self.targets):
            self.complete = True
            db.add(self)
            db.commit()
