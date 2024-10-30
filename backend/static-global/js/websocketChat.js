const username = document.querySelector('#username').value

const chatSocket = new WebSocket(
    'ws://' + window.location.host + `/ws/chat?username=${username}`,)

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data)
    console.log(`Dados Mensagem: ${Object.getOwnPropertyNames(data)}`)
    console.log(`Quem: ${data.sender_username}, Quando: ${data.time} e o que: ${data.message}`)
    
    document.querySelector('#chat-log').innerHTML += (`
        <li class="${data.sender_username == username ? 'selfMessage':'otherMessage'}">
            ${data.message}
        </li>
    `)
}

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly')
}

document.querySelector('#chat-message-input').focus()
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {
        document.querySelector('#chat-message-submit').click()
    }
}

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = document.querySelector('#chat-message-input').value;
    
    chatSocket.send(JSON.stringify({
        'chat': '45eb0679-6625-40f7-8a6e-4208f9691280',
        'message': message
    }))
    messageInputDom.value = ''
}