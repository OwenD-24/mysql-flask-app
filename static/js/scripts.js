// Get modal and open button
var modal = document.getElementById("noteModal");
var btn = document.getElementById("openModalBtn");
var span = document.getElementsByClassName("close")[0];

// Open the modal when the button is clicked
btn.onclick = function() {
    modal.style.display = "block";
}

// Close the modal when the close button is clicked
span.onclick = function() {
    modal.style.display = "none";
}

// Close the modal if the user clicks outside the modal content
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

