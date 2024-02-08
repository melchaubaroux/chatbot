
async function addNewQuestion () { 

  // add question 
  const question = prompt("posez votre question");
  const newquestionEl =document.createElement("p",{'class':"question"});
  newquestionEl.innerText=question;
  const conversationEl =document.getElementById("conversation");
  conversationEl.appendChild(newquestionEl);

  // test 1 connection with api error 422 
  // const answertestEl = document.createElement("p",{class:"reponse"});
  // answertestEl.innerText = test(question);
  // conversationEl.appendChild(answertestEl);


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
  // console.log(text);
  
  const apiUrl = "http://localhost:8000/chatbot?text=" + encodeURIComponent(text);
  
  return fetch(apiUrl,{method:"POST"})

  
  }

  








// function give_answer(question){
//     // recupere la reponse 
//         fetch('http://127.0.0.1:8000/docs#/default/chatbot_chatbot_post'),
//                 {
//                 method: "Post",
//                 body: JSON.stringify({ body: question,}),
//                 headers: { "Content-type": "application/json", charset:"UTF-8"},
//                 }
//         .then(response => response.json())
//         .then((json) => console.log(json));

//     // integre la reponse la reponse 
//     const answerEl = document.createElement("p",{class:"reponse"});
//     answerEl.innerText = reponse;
//     conversation.appendChild(answerEl);


//     }

  
    // function give_answer(question){
    //     // recupere la reponse 
    //     console.log('give answer');
    //         fetch('http://127.0.0.1:8000/docs#/default/chatbot_chatbot_post', {
    //                 method: "POST",
    //                 body: JSON.stringify({ 'text': question}),
    //                 headers: {"Content-Type": "application/json"},
    //                 }).then(response => response.json())
    //     .then(data => {
    //         console.log("Success:", data);
    //         return data;  // Retourner les données pour les utiliser dans le code appelant
    //     })
    //     .catch(error => {
    //         console.error("Error:", error);
    //         return { error: "Une erreur s'est produite lors de la requête à l'API." };
    //     });
        
  
    //   }
      

