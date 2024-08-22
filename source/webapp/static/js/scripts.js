function performAction(action) {
    let numberA = document.getElementById('numberA').value;
    let numberB = document.getElementById('numberB').value;
    let resultBlock = document.getElementById('result');

    fetch(`/${action}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'  // CSRF защита
        },
        body: JSON.stringify({
            "A": parseFloat(numberA),
            "B": parseFloat(numberB)
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.answer !== undefined) {
                resultBlock.textContent = `Answer: ${data.answer}`;
                resultBlock.classList.add('success');
                resultBlock.classList.remove('error');
            } else if (data.error) {
                resultBlock.textContent = `Error: ${data.error}`;
                resultBlock.classList.add('error');
                resultBlock.classList.remove('success');
            }
        })
        .catch(error => {
            resultBlock.textContent = `Error: ${error}`;
            resultBlock.classList.add('error');
            resultBlock.classList.remove('success');
        });
}