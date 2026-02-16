from storage.database import SessionLocal
from storage.event_repository import Event

def handle_sip(payload: dict):
    
    print("SIP handler triggered")
    
    db = SessionLocal()
    
    event = Event(
        event_type = "sip.call_event",
        call_id = payload.get("call_id"),
        sip_status = payload.get("sip_status"),
        payload=payload
    )
    
    db.add(event)
    db.commit()
    db.close()
    
    print("SIP event inserted into DB")