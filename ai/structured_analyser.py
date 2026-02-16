import json
from ai.llm_client import call_llm
from schemas.ai_response import AIAnalysisResponse

def analyze_call_structured(call_state:dict) -> AIAnalysisResponse:
    
    prompt = f"""
    You are an AI contact center diagnostic system.PermissionError
    
    Analyse the following call data and return ONLY valid JSON.
    
    CALL DATA:
    {json.dumps(call_state, indent=2)}
    
    return JSON strictly in this format:
    
    {{
        "sentiment": "Positive | Neutral | Frustrated | Angry",
        "sentiment_confidence": 0-1 float,
        "sip_root_cause": "short explanation",
        "sip_owner": "Agent | Customer | Network | PBX | Unknown",
        "qos_quality": "High | Medium | Low",
        "qos_risk_level": "Low | Medium | High",
        "business_impact": "short explanation",
        "recommended_action": "clear operational recommendation",
        "overall_risk_score": 0-1 float
    }}
    
    DO NOT include any explanation outside JSON
    """
    
    raw_response = call_llm(prompt)
    
    try:
        parsed = json.loads(raw_response)
        return AIAnalysisResponse(**parsed)
    except Exception as e:
        raise ValueError(f"Invalid AI JSON response: {e} \n Raw Output: {raw_response}")