import json
from ai.llm_client import call_llm
from schemas.ai_response import AIAnalysisResponse

def analyze_call_structured(call_state:dict) -> AIAnalysisResponse:
    
    prompt = f"""
    You are an AI contact center diagnostic system.
    
    You must analyse THREE independent domains:
    
    1. CUSTOEMR SENTIMENT (use transcript only)
    2. SIP DIAGNOSTICS (use sip_status and disconnect_reason only)
    3. MEDIA QUALITY (use packet_loss, jitter, mos_score only)
    
    IMPORTANT RULES:
    - Do NOT mix transcript data into SIP analysis.
    - Do Not mix business context into SIP root cause.
    - SIP root cause must strictly reflect SIP signalling behavior.
    - if SIP data is insufficient, set sip_owner to "Unknown"
    
    CALL DATA:
    {json.dumps(call_state, indent=2)}
    
    return JSON strictly in this format:
    
    {{
        "sentiment": one of ["Positive", "Neutral", "Frustrated", "Angry"],
        "sentiment_confidence": float between 0 and 1,
        "sip_root_cause": short technical explanation,
        "sip_owner": one of ["Agent", "Customer", "Network", "PBX", "Unknown"],
        "qos_quality": one of ["High", "Medium", "Low"],
        "qos_risk_level": one of ["Low", "Medium", "High"],
        "business_impact": short explanation,
        "recommended_action": clear operational recommendation,
        "overall_risk_score": float between 0 and 1
    }}
    
    DO NOT include any explanation outside JSON
    """
    
    raw_response = call_llm(prompt)
    
    try:
        parsed = json.loads(raw_response)
        return AIAnalysisResponse(**parsed)
    except Exception as e:
        raise ValueError(f"Invalid AI JSON response: {e} \n Raw Output: {raw_response}")