from storage.database import SessionLocal
from storage.event_repository import Event
from schemas.canonical_call import CanonicalCallState

def build_call_state(call_id: str) -> CanonicalCallState:
    
    db = SessionLocal()
    
    events = db.query(Event).filter(Event.call_id == call_id).all()
    
    db.close()
    
    
    state = {
        "call_id": call_id,
        "queue": None,
        "duration": None,
        "sip_status": None,
        "disconnect_reason": None,
        "packet_loss": None,
        "jitter": None,
        "mos_score": None,
    }
    
    for event in events:
        payload = event.payload
        
        if event.event_type == "conversation.completed":
            state["queue"] = payload.get("queue")
            state["duration"] = payload.get("duration")
            state["transcript"] = payload.get("transcript")
            
        elif event.event_type == "sip.call_event":
            state["sip_status"] = payload.get("sip_status")
            state["disconnect_reason"] = payload.get("disconnect_reason")
            
        elif event.event_type == "media.quality":
            state["packet_loss"] = payload.get("packet_loss")
            state["jitter"] = payload.get("jitter")
            state["mos_score"] = payload.get("mos_score")
            
    return CanonicalCallState(**state)