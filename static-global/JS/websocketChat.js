const username = document.querySelector('#username').value

const chatSocket = new WebSocket(
    'ws://' + window.location.host + `/ws/chat/${username}/`)

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data)
    document.querySelector('#chat-log').innerHTML += ('<br>' + data.message)
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
        'message': message
    }))
    messageInputDom.value = ''
}