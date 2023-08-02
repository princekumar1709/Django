// scripts.js
function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    // Save the data of the dragged column
    event.dataTransfer.setData('text', event.target.dataset.column);
}

function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData('text');
    
    // Create a graph element based on the dropped column
    createGraph(data, event.target);
}

function createGraph(columnName, targetElement) {
    // Here, you can use a JavaScript library (e.g., Chart.js, Plotly) to create the graph
    // For simplicity, I'll just append the column name to the targetElement as an example.
    var graphElement = document.createElement('div');
    graphElement.classList.add('graph');
    graphElement.textContent = 'Graph for Column: ' + columnName;
    targetElement.appendChild(graphElement);
}
 