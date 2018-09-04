
// Script para actualizacion de las muestras segun la frecuencia elegida
  var counter = 0;
  var idInter=-1;        
            // Funcion para tomar la frecuencia
            function selectfrequency()
            {
                var x = document.getElementById("frec");
                var strUser = x.options[x.selectedIndex].value;
                var interval = (Number(strUser)*1000);
                console.log(idInter);
                $("#cartel").text("Actualizando cada "+ strUser + " segundos")  
                if (idInter != -1){ 
                    window.clearInterval(idInter); 
                }
                // var interval = strUser*1000;
                idInter = window.setInterval('refreshDiv()', interval);

            }
            // Funcion para refrescar el Div
            function refreshDiv(){
                counter = counter + 1;
                console.log(counter);
                 $.get("/avgjson", function(data) {
                // $("#id").text(data.id);
                $("#tempavg").text(data.temperature+" °C");
                $("#humavg").text(data.humidity+" %");
                $("#windavg").text(data.windspeed+" km/h");
                $("#pressavg").text(data.pressure+" hPa");
                $("#idtemp").text(data.lasttemp+" °C");
                $("#idhum").text(data.lasthum+" %");
                $("#idwind").text(data.lastwind+" km/h");
                $("#idpress").text(data.lastpress+" hPa");            
                });

                
            }