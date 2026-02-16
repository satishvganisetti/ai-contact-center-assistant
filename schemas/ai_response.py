from pydantic import BaseModel, Field
from typing import Literal

class AIAnalysisResponse(BaseModel):
    sentiment: Literal["Positive", "Neutral", "Frustrated", "Angry"]
    sentiment_confidence: float = Field(ge=0, le=1)
    
    sip_root_cause: str
    sip_owner: Literal["Agent", "Customer", "Network", "PBX", "Unknown"]
    
    qos_quality: Literal["High", "Medium", "Low"]
    qos_risk_level: Literal["Low", "Medium", "High"]
    
    business_impact: str
    recommended_action: str
    
    overall_risk_score: float = Field(ge=0, le=1)