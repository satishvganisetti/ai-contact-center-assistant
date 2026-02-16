from pydantic import BaseModel, Field

class MediaQualityPayload(BaseModel):
    call_id: str
    packet_loss: float = Field(ge=0)
    jitter: float = Field(ge=0)
    mos_score: float = Field(ge=1, le=5)