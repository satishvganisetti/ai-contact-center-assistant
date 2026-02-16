from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from ingestion.dispatcher import dispatch_event

router = APIRouter()

class WebhookEvent(BaseModel):
    event_type: str
    payload: Dict[str, Any]
    
@router.post("/webhook")
def receive_event(event: WebhookEvent):
    try:
        print("Received Event: ", event.event_type)
        dispatch_event(event.event_type, event.payload)
        return {"Status": "Processed"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))