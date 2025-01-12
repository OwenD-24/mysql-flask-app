// Get the modal, the button that opens it, and the close span
var modal = document.getElementById('noteModal');
var btn = document.getElementById('openModalBtn');
var span = document.getElementsByClassName('close')[0];

// When the user clicks the "Add Note" button, open the modal
btn.onclick = function() {
    modal.style.display = 'block';
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = 'none';
}

// When the user clicks anywhere outside the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Update the transaction amount based on the selected payment plan
function updateAmount() {
    var paymentPlan = document.getElementById('payment_plan');
    var selectedOption = paymentPlan.options[paymentPlan.selectedIndex];
    var price = selectedOption.getAttribute('data-price');
    document.getElementById('transaction_amount').value = price;
}
