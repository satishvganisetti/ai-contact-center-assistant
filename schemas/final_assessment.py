from pydantic import BaseModel
from schemas.ai_response import AIAnalysisResponse

class FinalCallAssessment(AIAnalysisResponse):
    requires_escalation: bool