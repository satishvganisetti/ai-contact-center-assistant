from sqlalchemy import Column, Integer, String, Float, Boolean, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from storage.database import Base

class AIInvocationLog(Base):
    __tablename__ = "ai_invocations"
    
    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(String, index=True)
    
    model_name = Column(String)
    latency_ms = Column(Float)
    
    prompt_hash = Column(String)
    
    raw_response = Column(Text)
    structured_output = Column(JSONB)
    
    overall_risk_score = Column(Float)
    requires_escalation = Column(Boolean)

    error_message = Column(Text, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    