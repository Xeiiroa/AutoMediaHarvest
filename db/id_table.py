import os

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class MediaIdTable(Base):
    __tablename__ = 'mediaIds'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    mediaId: Mapped[str] = mapped_column(String)
    #? do i have to create a variable to append the ids to
    
    
    