from storage.database import SessionLocal
from storage.event_repository import Event

def handle_media(payload: dict):
    print("Media handler triggered")
    
    db = SessionLocal()
    
    event = Event(
        event_type = "media.quality",
        call_id = payload.get("call_id"),
        mos_score = payload.get("mos_score"),
        payload=payload
    )
    
    db.add(event)
    db.commit()
    db.close()
    
    print("Media event inserted into DB")