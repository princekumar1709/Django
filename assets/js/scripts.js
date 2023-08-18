// scripts.js
function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    // Save the data of the dragged field name
    event.dataTransfer.setData('text/plain', event.target.classList.contains('rows'));
}

function drop(event) {
    event.preventDefault();

    var targetDiv = event.target;
    if (targetDiv.classList.contains('input')) {
        var data = event.dataTransfer.getData('text/plain');
        var draggedElement = document.createElement('div'); // Create a new div
        draggedElement.className = 'rows'; // Apply the appropriate class
        draggedElement.textContent = data; // Set the text content
        
        targetDiv.appendChild(draggedElement);
    }
}



