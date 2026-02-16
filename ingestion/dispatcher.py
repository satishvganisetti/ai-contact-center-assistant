from schemas.conversation_schema import ConversationPayload
from schemas.sip_schema import SIPPayload
from schemas.media_schema import MediaQualityPayload

from ingestion.conversation_handler import handle_conversation
from ingestion.sip_handler import handle_sip
from ingestion.media_handler import handle_media

def dispatch_event(event_type: str, payload: dict):
    
    if event_type == "conversation.completed":
        validated = ConversationPayload(**paylaod)
        return handle_conversation(validated.dict())
    
    elif event_type == "sip.call_event":
        validated = SIPPayload(**payload)
        return handle_sip(validated.dict())
    
    elif event_type == "media.quality":
        validated = MediaQualityPayload(**payload)
        return handle_media(validated.dict())
    
    else:
        raise ValueError(f"Unsupported event type: {event_type}")        