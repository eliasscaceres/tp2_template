
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
                
                if (idInter != -1){ 
                    window.clearInterval(idInter); 
                }
                // var interval = strUser*1000;
                idInter = window.setInterval('refreshDiv()', interval);

            }
            // Funcion para refrescar el Div
            function refreshDiv(){
                counter = counter + 1;
                $.get("/lastjson/", function(data) {
        		// $("#id").text(data.id);
        		$("#idtemp").text(data.temperature+" °C");
                $("#idhum").text(data.humidity+" %");
                $("#idwind").text(data.windspeed+" km/h");
        		$("#idpress").text(data.pressure+" hPa");
        	
        		
        		});

                
            }