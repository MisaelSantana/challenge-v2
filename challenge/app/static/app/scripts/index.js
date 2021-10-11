// Functions JavaScript;

// Function for clear form;
function clearForm() {
    with (document) {
        document.getElementById('partida').value = "";
        document.getElementById('destino').value = "";
        document.getElementById('km40').value = "";
        document.getElementById('km60').value = "";
        document.getElementById('km80').value = "";
        document.getElementById('km100').value = "";
    }
}

// Function for push data end calculate;
function calculated() {
    // After calculated end to send data, this function server to clear the fields;
    with (document) {
        document.getElementById('partida').value = "";
        document.getElementById('destino').value = "";
        document.getElementById('km40').value = "";
        document.getElementById('km60').value = "";
        document.getElementById('km80').value = "";
        document.getElementById('km100').value = "";
    }
}