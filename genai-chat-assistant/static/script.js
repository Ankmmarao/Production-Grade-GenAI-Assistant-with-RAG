async function sendMessage(){

let input = document.getElementById("message")

let message = input.value

if(message === "") return

document.getElementById("chatbox").innerHTML +=
"<p><b>You:</b> "+message+"</p>"

let response = await fetch("/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:message
})

})

let data = await response.json()

document.getElementById("chatbox").innerHTML +=
"<p><b>Assistant:</b> "+data.reply+"</p>"

input.value=""
}