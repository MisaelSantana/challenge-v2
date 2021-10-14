// Call function python for get inputs and push for backend
//$.ajax({
//    type: "POST",
//    url: "~/apiData.py",
//    data: { "returnObject": destino}
//}).done(function (o) {
//    return data
//})


//$.ajax({
//    type: "POST",
//    url: "~/apiData.py",
//    data: { "destino": destino },
//    success: function (response) {
//        alert(response);
//    }
//});

function getData() {
    return $.ajax({
        type: "POST",
        url: "/Api/Data/Calculate/",
        data: "partida=Casa&destino=Seven&km40=40&km60=93&km80=95&km100=900"
    });
};

//function showData() {
//    /*console.log(data.responsejson)*/
//    //let teste = {
//    //    //document.getElementById('partida').value = data.responseJSON['partida'];
//    //    //document.getElementById('destino').value = data.responseJSON['destino'];
//    //    //document.getElementById('km40').value = data.responseJSON['km40'];
//    //    //document.getElementById('km60').value = data.responseJSON['km60'];
//    //    //document.getElementById('km80').value = data.responseJSON['km80'];
//    //    //document.getElementById('km100').value = data.responseJSON['km100'];

//    //    //partida: document.getElementById('partida').value = data.responseJSON['partida'],
//    //    //destino: document.getElementById('destino').value = data.responseJSON['destino'],
//    //    //km40: document.getElementById('km40').value = data.responseJSON['km40'],
//    //    //km60: document.getElementById('km60').value = data.responseJSON['km60'],
//    //    //km80: document.getElementById('km80').value = data.responseJSON['km80'],
//    //    //km100: document.getElementById('km100').value = data.responseJSON['km100'],
//    //}
//    //console.log(teste.responseJSON)
//    data = getData()

//    document.getElementById('partida').value = data.responseJSON['partida'];
//    document.getElementById('destino').value = data.responseJSON['destino'];
//    document.getElementById('km40').value = data.responseJSON['km40'];
//    document.getElementById('km60').value = data.responseJSON['km60'];
//    document.getElementById('km80').value = data.responseJSON['km80'];
//    document.getElementById('km100').value = data.responseJSON['km100'];

//};

//window.onload = showData()

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
};

// Function for push data end calculate;
function calculated() {
    data = getData();

    

    // After calculated end to send data, this function server to clear the fields;
    with (document) {
        document.getElementById('partida').value = "";
        document.getElementById('destino').value = "";
        document.getElementById('km40').value = "";
        document.getElementById('km60').value = "";
        document.getElementById('km80').value = "";
        document.getElementById('km100').value = "";
    }
};