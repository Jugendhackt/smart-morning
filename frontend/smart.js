let time;
const enter =document.getElementById('enter');
const input=['licht','heitzung', 'kaffemaschine','rolläden','computer' ];
const body = document.getElementsByTagName('body');



window.addEventListener('load',bild);
window.addEventListener('resize',bild);
function bild(){
    console.log(body);
    if(window.innerWidth>900){
        document.body.style.backgroundImage='url(https://cdn.pixabay.com/photo/2016/11/18/14/40/balcony-1834990_960_720.jpg)';
    }else{
        document.body.style.backgroundImage='url(https://cdn.pixabay.com/photo/2021/08/06/17/06/breakfast-6526807_960_720.jpg)';
    }
}


function visible(whichInput) {
    time = document.getElementById(whichInput);
    if (time.style.display == 'inline') {
        time.style.display = 'none';
    } else {
        time.style.display = 'inline';
    }
}

enter.addEventListener('click',function(){
    console.log(window.innerWidth);
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
       url: "http://127.0.0.1:5000/send",
       contentType: "application/json",
       data: JSON.stringify({
        wakeup_time: weckZeit,
        device_timings: output,
        enabled: true
       }),
       dataType: "json",
   });
  
})





