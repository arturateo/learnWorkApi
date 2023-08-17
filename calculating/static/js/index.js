async function makeRequest(url, body = null, method) {
    let headers = {};
    let response
    if (method !== "GET") {
        const csrftoken = getCookie('csrftoken');
        headers = {
            'X-CSRFToken': csrftoken, 'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = await fetch(url, {
            "method": method,
            'body': JSON.stringify(body),
            "headers": headers
        });
    } else {
        response = await fetch(url, {
            "method": method,
            "headers": headers
        });
    }
    if (response.ok) {
        return await response.json();
    } else {
        let result = await response.json();
        let result_html = document.getElementById('result')
        result_html.innerText = result.error
        result_html.className = "text-danger"
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function onClick(event) {
    event.preventDefault()
    let button = event.target;
    let url = button.dataset.url
    let method = button.dataset.method
    let body = {
        "A": document.getElementById('number_1').value,
        "B": document.getElementById('number_2').value,
    }
    let result = await makeRequest(url, body, method);
    let result_html = document.getElementById('result')
    result_html.innerText = result.answer

}

function onLoad() {
    let buttons = document.getElementsByClassName("calculating")
    for (let button of buttons) {
        button.addEventListener("click", onClick)
    }
}

window.addEventListener('load', onLoad)