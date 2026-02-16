from schemas.ai_response import AIAnalysisResponse
from schemas.final_assessment import FinalCallAssessment

def apply_risk_rules(ai_result: AIAnalysisResponse) -> FinalCallAssessment:

    data = ai_result.model_dump()

    # Deterministic overrides
    if data["qos_risk_level"] == "High":
        data["overall_risk_score"] = max(data["overall_risk_score"], 0.8)

    if data["sentiment"] == "Angry":
        data["overall_risk_score"] = max(data["overall_risk_score"], 0.85)

    if data["sip_owner"] == "Network":
        data["recommended_action"] += " | Escalate to network operations team."

    # Escalation decision
    data["requires_escalation"] = data["overall_risk_score"] >= 0.75

    return FinalCallAssessment(**data)