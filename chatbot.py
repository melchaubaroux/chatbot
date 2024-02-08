import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODAwMTFhYmEtYzNlNy00YzY5LTliZGMtMGQ5OThkODk2OWU1IiwidHlwZSI6ImFwaV90b2tlbiJ9.N3jUN6ucg324ejC2D9BYZNTAi0awJ4BWdLsXqva1164"}
url = "https://api.edenai.run/v2/text/chat"


def send_text (text,context=[],main_model="openai", behavior="Act as an jackass"):

    payload = {
        "providers":main_model,
        "text": text,
        "chatbot_global_action":behavior ,
        "previous_history": context,
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result= json.loads(response.text)
    
    return result



def chatbot():

    context=[]
   
    while True : 

        text=input("posez votre question :  ")

        if text=="quit":
            break

        out=send_text (text,context)
        
        model=list(out.keys())[0]

        for x in range(len(out[model]['message'])): 
            context+=[out[model]['message'][x]]

        print(out[model]['generated_text'])

    return context
       
chatbot()