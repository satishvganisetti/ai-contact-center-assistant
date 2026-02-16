from pydantic import BaseModel

class SIPPayload(BaseModel):
    call_id: str
    sip_status: int
    disconnect_reason: str