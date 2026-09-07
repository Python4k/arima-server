import enum
from typing import List
import uuid
from sqlalchemy import Enum, ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

class Roles(enum.Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )
    messages: Mapped[List["Message"]] = relationship()

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )
    role: Mapped[Roles] = mapped_column(Enum(Roles), nullable=False)
    conversation_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("conversations.id"), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)