// scripts.js
function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    // Save the data of the dragged field name
    event.dataTransfer.setData('text/plain', event.target.innerText);
}

function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData('text/plain');

    // Append the dropped field name to the target div
    var targetDiv = event.target;
    if (targetDiv.classList.contains('input')) {
        targetDiv.innerHTML += '<div>' + data + '</div>';
    }
}
