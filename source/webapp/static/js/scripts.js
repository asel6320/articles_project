async function makeRequest(url, method = "GET") {
    let response = await fetch(url, { method: method });
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(await response.text());
        console.log(error);
        throw error;
    }
}

async function onClick(event) {
    event.preventDefault();
    let button = event.target.closest('button.like-button');  // Get the clicked button
    let url = button.dataset.url;  // Get the URL from the data-url attribute

    try {
        let response = await makeRequest(url);
        let likeCountSpan = button.querySelector(".like-count");

        // Update the like count
        likeCountSpan.innerText = response.like_count;

        // Update the button text based on the like status
        if (response.liked) {
            button.innerHTML = `Unlike (<span class="like-count">${response.like_count}</span>)`;
        } else {
            button.innerHTML = `Like (<span class="like-count">${response.like_count}</span>)`;
        }

        console.log(response);
    } catch (error) {
        console.error("Request failed", error);
    }
}

function onLoad() {
    let buttons = document.querySelectorAll('.like-button');
    for (let button of buttons) {
        button.addEventListener("click", onClick);
    }
}

window.addEventListener("load", onLoad);