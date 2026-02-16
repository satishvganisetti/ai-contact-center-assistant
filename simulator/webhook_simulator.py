import requests
import random

URL = "http://127.0.0.1:8000/webhook"

def send_conversation_event():
    event ={
        "event_type": "conversation.completed",
        "payload": {
            "call_id": "call_001",
            "duration": 300,
            "queue": "Billing Support"
        }
    }
    
    requests.post(URL,json=event)
    
    if __name__ == "__main__":
        send_conversation_event()