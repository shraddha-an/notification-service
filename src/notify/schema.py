"""Contains data schemas for messages intended for notification channels."""

from pydantic import BaseModel

class Message(BaseModel):
    subject: str
    body: str