var today = new Date();
var hours = today.getHours();

$(document).ready(function(){
    //console.log("OK!");
    var usuario = $('#saludo').text();
    if(hours > 12){
        if(hours > 18){
            $('#saludo').text("Buenas Noches, " + usuario)
            }else{
            $('#saludo').text("Buenas Tardes, " + usuario)
        }
        }else{
        $('#saludo').text("Buenos Días, " + usuario)
    }

})