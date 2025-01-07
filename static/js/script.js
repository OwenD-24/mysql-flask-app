// Get references to the modal, button, and close span elements
var modal = document.getElementById("myModal"); // The modal container
var btn = document.getElementById("openModalBtn"); // The button that triggers the modal
var span = document.getElementsByClassName("close")[0]; // The "close" span to close the modal

// When the button is clicked, show the modal by setting its display to "flex"
btn.onclick = function() {
    modal.style.display = "flex";
}

// When the "close" button (span) is clicked, hide the modal by setting display to "none"
span.onclick = function() {
    modal.style.display = "none";
}

// When clicking anywhere outside the modal, close it if the target is the modal background
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}