from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from storage.database import Base

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, index=True, nullable=False)
    call_id = Column(String, index=True, nullable=False)
    
    #structured columns
    queue = Column(String, nullable=True)
    duration = Column(Integer, nullable=True)
    sip_status = Column(Integer, nullable=True)
    mos_score = Column(Float, nullable=True)
    
    #raw JSON Payload
    payload = Column(JSONB, nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())