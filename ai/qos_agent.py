from ai.llm_client import call_llm

def analyze_qos(packet_loss: float, jitter: float, mos_score: float) -> str:
    prompt = f"""
    Media quality metrics:
    Packet Loss: {packet_loss}%
    Jitter: {jitter} ms
    MOS Score: {mos_score}
    
    Assess cakk quality and risk level (Mow, Medium, High).
    """
    
    return call_llm(prompt)