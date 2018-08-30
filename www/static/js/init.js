

  var counter = 0;
  var idInter=-1;        
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
                idInter = window.setInterval("refreshDiv()", interval);

            }
            function refreshDiv(){
                counter = counter + 1;
                $.get("/lastjson/", function(data) {
        		$("#id").text(data.id);
        		$("#idtemp").text(data.temperature);
        		$("#idpress").text(data.pressure);
        		$("#idhum").text(data.humidity);
        		$("#idwind").text(data.windspeed);
        		});

                document.getElementById("test").innerHTML = "Testing " + counter;
            }