from storage.database import SessionLocal
from storage.event_repository import Event

def handle_conversation(payload: dict):
    db = SessionLocal()
    
    event = Event(
        event_type = "conversation.completed",
        call_id = payload.get("call_id"),
        queue=payload.get("queue"),
        duration=payload.get("duration"),
        payload=payload
    )
    
    db.add(event)
    db.commit()
    db.close()
    
    print("Conversation event stored")