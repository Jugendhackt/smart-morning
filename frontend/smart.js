let time;
const enter = document.getElementById('enter');
const input = ['licht', 'heizung', 'kaffeemaschine', 'rollläden', 'pc'];
const body = document.getElementsByTagName('body');
const list = document.querySelectorAll('#list li');

window.addEventListener('load', bild);
window.addEventListener('resize', bild);
function bild() {
    if (window.innerWidth > 1100) {
        document.body.style.backgroundImage = 'url(https://cdn.pixabay.com/photo/2016/11/18/14/40/balcony-1834990_960_720.jpg)';
    } else {
        document.body.style.backgroundImage = 'url(https://cdn.pixabay.com/photo/2021/08/06/17/06/breakfast-6526807_960_720.jpg)';
    }
}
for (let i = 0; i < list.length; i++) {
    list[i].children[1].addEventListener("click", function () {
        time = list[i].children[2];
        if (time.style.display == 'inline') {
            time.style.display = 'none';
        } else {
            time.style.display = 'inline';
        }
    })
}
enter.addEventListener('click', function () {
    var output = [];
    const weckZeit = document.getElementById('wecker').value;
    if (weckZeit == '') {
        document.getElementById('uhrzeit').innerHTML = 'Bitte gebe eine Weckzeit an';
        return
    } else if (weckZeit !== '') {
        document.getElementById('uhrzeit').innerHTML = '';
    }
    document.getElementById('info').innerHTML = `dein Wecker klingelt morgen um ${weckZeit}`;
    for (let n = 0; n < input.length; n++) {
        if (document.getElementById(input[n] + 'Zeit').style.display == 'inline') {
            if (document.getElementById(input[n] + 'Zeit').value == '') {
                document.getElementById(input[n] + 'Zeit').value = 0;
            }
            output.push([input[n], document.getElementById(input[n] + 'Zeit').value]);
        }
    }
    $.ajax({
        type: "POST",
        url: "http://192.168.4.131:5000/send",
        contentType: "application/json",
        data: JSON.stringify({
            wakeup_time: weckZeit,
            device_timings: output,
            enabled: false
        }),
        dataType: "json",
    });

})





