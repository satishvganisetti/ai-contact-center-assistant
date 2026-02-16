from ai.llm_client import call_llm

def analyze_sentiment(transcript: list) -> str:
    
    conversation_text = "\n".join(
        f"{u['speaker']}: {u['text']}" for u in transcript
    )
    
    prompt = f"""
    Analyze the sentiment of the customer in the following conversation.
    Classify as: Positive, Neutral, Frustrated, Angry.
    
    conversation:
    {conversation_text}
    """
    
    return call_llm(prompt)