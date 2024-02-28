
async function addNewQuestion () { 

  // add question 
  const question = prompt("posez votre question");
  const newquestionEl =document.createElement("p",{'class':"question"});
  newquestionEl.innerText=question;
  const conversationEl =document.getElementById("conversation");
  conversationEl.appendChild(newquestionEl);

  // add response 
  const answerEl = document.createElement("p",{class:"reponse"});
  answerEl.innerText = await give_answer(question).then(response => response.text()).catch(error => { console.error('Error:', error)});                                                                                                                         
  conversationEl.appendChild(answerEl);


}

function test(question){
  console.log('test endpoints');
        fetch('http://127.0.0.1:8000/test?text='+encodeURIComponent(question), {
                method: "GET"

                }).then(response => {return response.json()});
}


async function give_answer(question){
  const text = question;
  
  const apiUrl = "http://localhost:8000/chatbot?text=" + encodeURIComponent(text);
  
  return fetch(apiUrl,{method:"POST"})

  }
