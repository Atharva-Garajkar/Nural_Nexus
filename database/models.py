# This contains all the models

from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, DateTime, func
from sqlalchemy.sql import func
from datetime import datetime


#Creation of Database
class Session( SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory = datetime.utcnow)
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True),server_default=func.now(), onupdate=func.now()))
    messages: List["Message"] = Relationship(back_populates= "session")

    channel_id: str = Field(default="general_channel", description="Channel identifier")

    is_dm: bool = Field(default=False, description="Indicates if the session is a direct message")


    delete: bool = Field(default=False)

class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key = True)

    created_at: datetime = Field(default_factory=datetime.utcnow)
    author: str
    text: str

    session_id: Optional[int] = Field(default=None, foreign_key= "session.id") 
    session: Optional[Session] = Relationship(back_populates = "messages")