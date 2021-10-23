let time;
const enter =document.getElementById('enter');
const input=['licht','heitzung', 'kaffemaschine','rolläden','computer' ];




function visible(whichInput) {
    time = document.getElementById(whichInput);
    if (time.style.display == 'inline') {
        time.style.display = 'none';
    } else {
        time.style.display = 'inline';
    }
}

enter.addEventListener('click',function(){
    var output=[];
    const weckZeit= document.getElementById('wecker').value;
    if(weckZeit==''){
        document.getElementById('uhrzeit').innerHTML='Bitte gebe eine Weckzeit an';
        return
    }else if(weckZeit !==''){
        document.getElementById('uhrzeit').innerHTML='';
    }
    document.getElementById('info').innerHTML=`dein Wecker klingelt morgen um ${weckZeit}`;
   for(let n=0;n<input.length;n++){
       if(document.getElementById(input[n]+'Zeit').style.display=='inline'){
           if(document.getElementById(input[n]+'Zeit').value==''){
            document.getElementById(input[n]+'Zeit').value=0;
           }
           output.push([input[n],document.getElementById(input[n]+'Zeit').value]);
       }
   }
   $.ajax({
       type: "POST",
       url: "http://192.168.4.91:5000/send",
       contentType: "application/json",
       data: JSON.stringify({
        wakeup_time: weckZeit,
        device_timings: output,
        enabled: true
       }),
       dataType: "json",
   });
  
})





