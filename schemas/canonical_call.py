from pydantic import BaseModel
from typing import Optional, List, Dict

class CanonicalCallState(BaseModel):
    call_id: str
    
    #Business
    queue: Optional[str]
    duration: Optional[int]
    
    #Technical
    sip_status: Optional[int]
    disconnect_reason: Optional[str]
    
    #Media
    packet_loss: Optional[float]
    jitter: Optional[float]
    mos_score: Optional[float]
    
    transcript: Optional[list[Dict]] = None