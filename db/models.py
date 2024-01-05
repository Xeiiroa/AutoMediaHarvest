import os
import pathlib

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Settings(Base):
    default_video_path = os.getcwd()
    
    __tablename__ = 'user_info'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    video_save_path: Mapped[str] = mapped_column(String, server_default=default_video_path + '/media')
    album_name: Mapped[str] = mapped_column(String, server_default='AutoMediaHarvest')