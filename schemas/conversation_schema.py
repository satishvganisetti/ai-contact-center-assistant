from pydantic import BaseModel, Field
from typing import List

class Utterance(BaseModel):
    speaker: str
    text: str
    
class ConversationPayload(BaseModel):
    call_id: str
    queue: str
    duration: int = Field(gt=0)
    transcript: List[Utterance]