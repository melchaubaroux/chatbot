from fastapi import FastAPI
import json
import requests
import uvicorn
from bs4 import BeautifulSoup


# with open('history','w') as f : 
#     f.write("")

# json.dumps('history',"")



headers = {"Authorization": ""}
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



app=FastAPI()


from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
    )

@app.get("/test")
def test(prompt): 
    return "salut "+prompt


@app.post("/chatbot")
def chatbot(text):
    context=[]
    # response = requests.get("http://127.0.0.1:8001/")
    # soup = BeautifulSoup(response.text, 'html.parser')
    

    # for x in zip(soup.find_all('chatbot question '),soup.find_all('chatbot reponse')):
        
    #     context+=[{'role':x[0],'message':x[1]}]

    # context+=[soup]
    
    # print(context)
    out=send_text (text,context)  
    model=list(out.keys())[0]

    return(out[model]['generated_text'])

    
uvicorn.run(app)



       
    

