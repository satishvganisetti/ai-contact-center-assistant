from ai.llm_client import call_llm

def analyze_sip(sip_status: int, disconnect_reason: str) -> str:
    
    prompt = f"""
    A call ended with the SIP status {sip_status}
    and disconnect reason '{disconnect_reason}'.
    
    Explain the likely cause and whether this is 
    customer-side, agent-side, or network issue or a component issue.
    """
    
    return call_llm(prompt)