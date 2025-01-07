document.getElementById("openModalBtn").onclick = function() {
    document.getElementById("noteModal").style.display = "block";
}

document.getElementsByClassName("close")[0].onclick = function() {
    document.getElementById("noteModal").style.display = "none";
}

window.onclick = function(event) {
    if (event.target == document.getElementById("noteModal")) {
        document.getElementById("noteModal").style.display = "none";
    }
}
