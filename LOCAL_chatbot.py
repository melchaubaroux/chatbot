import json
import requests
from asset import config 


headers=config.headers
url=config.url


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