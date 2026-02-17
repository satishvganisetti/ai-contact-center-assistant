from fastapi import FastAPI
from ingestion.webhook_handler import router
from storage.database import Base, engine
from storage import ai_invocation_repository
from storage import event_repository 

from processing.call_state_builder import build_call_state 
from ai.structured_analyser import analyze_call_structured
from ai.risk_engine import apply_risk_rules
from ai.observability import log_ai_invocation 

app = FastAPI(title= "AI Contact Center Assistant")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def health_check():
    return {"Status" : "Running"}

@app.get("/call-state/{call_id}")
def get_call_state(call_id: str):
    return build_call_state(call_id)

@app.get("/ai-analysis/{call_id}")
def analyze_call(call_id: str):
    
    call_state = build_call_state(call_id).dict()
    ai_result, raw_response, prompt, latency_ms = analyze_call_structured(call_state)
    final_result = apply_risk_rules(ai_result)
    
    log_ai_invocation(
        call_id=call_id,
        model_name="llama-3.1-8b-instant",
        prompt=prompt,
        raw_response=raw_response,
        structured_output=final_result.model_dump(),
        latency_ms=latency_ms
    )
    
    return final_result