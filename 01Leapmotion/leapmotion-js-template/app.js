const increment = 80;

var audioType = '.mp3'

    songs = ['clave', 'hihat', 'kick', 'rim', 'snare'];


function playAudio(drumNumber){
  var audioPlayer = document.getElementById('audio');
    audioPlayer.setAttribute('src', 'music/' + songs[drumNumber] + audioType);
    audioPlayer.setAttribute('controls', 'controls');
    audioPlayer.load();
    audioPlayer.play();
}

function getTrackNumber(pos) {
  if(pos != null) {
    var x = pos[0];
    var number = Math.floor((x+300)/increment);
    return number;
  }
}

function showDrumPlayed(number) {
  if(typeof number !== "undefined"){
    var i = document.getElementById(number.toString());
    if(i!=null) {
        i.style.fill = "#2c3e50";
        setTimeout(function() { i.style.fill="#ffffff" }, 100);
    }
  }
}

Leap.loop(function (frame) {
  if(frame.valid) {
    if(frame.gestures.length > 0){
      frame.gestures.forEach(function(gesture){
        switch (gesture.type){

          case "keyTap":
            var track = getTrackNumber(frame.gestures[0].position);
            console.log('playing track number ' + track);
            playAudio(track);
            showDrumPlayed(track);

          case "swipe":
            var track = getTrackNumber(frame.gestures[0].position);
            console.log('playing track number ' + track);
            playAudio(track);
            showDrumPlayed(track);
          }
      });
    } 
  }
});