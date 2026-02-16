import hashlib
import time
from storage.database import SessionLocal
from storage.ai_invocation_repository import AIInvocationLog

def log_ai_invocation(
    call_id: str,
    model_name: str,
    prompt: str,
    raw_response: str,
    structured_output: dict,
    latency_ms: float,
    error_message: str = None,
):
    
    db = SessionLocal()
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
    
    log = AIInvocationLog(
        call_id=call_id,
        model_name=model_name,
        latency_ms=latency_ms,
        prompt_hash=prompt_hash,
        raw_response=raw_response,
        structured_output=structured_output,
        overall_risk_score=structured_output.get("overall_risk_score"),
        requires_escalation=structured_output.get("requires_escalation"),
        error_message=error_message,
    )
    
    db.add(log)
    db.commit()
    db.close()