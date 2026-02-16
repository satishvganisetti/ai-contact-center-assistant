from ai.sentiment_agent import analyze_sentiment
from ai.sip_agent import analyze_sip
from ai.qos_agent import analyze_qos

def run_ai_analysis(call_state: dict) -> dict:
    
    results = {}
    
    if call_state.get("duration"):
        print("Calling sentiment agent")
        results["sentiment"] = analyze_sentiment(
            call_state.get("transcript", [])
        )
        
    if call_state.get("sip_status"):
        print("Calling sip agent")
        results["sip_analysis"] = analyze_sip(
            call_state.get("sip_status"),
            call_state.get("disconnect_reason")
        )
        
    if call_state.get("mos_score"):
        print("Calling Mos agent")
        results["qos_analysis"] = analyze_qos(
            call_state.get("packet_loss"),
            call_state.get("jitter"),
            call_state.get("mos_score")
        )
        
    return results