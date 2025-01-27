from pydantic import BaseModel, Field
from typing import List, Optional



class Turn(BaseModel):
    role: str
    content: str


class Conversation(BaseModel):
    model_name: str
    messages: List[Turn]


class EvaluationUnit(BaseModel):
    conversations: List[Conversation]


class ImageEvaluationUnit(BaseModel):
    conversation: Conversation
    image_url: str
    explanation: str