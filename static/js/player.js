/**
 * Created by mopdobopot on 14.05.14.
 */
$(document).ready(function() {

    var $tracks = $('.track'),
        isPlaying = false,
        curTrack,
        $curTrack,
        $curProgBar,
        $curTimer,
        curProgBarWidth,
        progBarUpdateTimer,
        curTrackIndex,
        curTrackId;

    var getAudio = function(sourceUrl) {
        var track = new Audio(sourceUrl);
        track.preload = true;
        setInterval(function() {
            $curTimer.html(getCurTrackTime());
        }, 1000);
        return track;
    };
    var applyPlayStyles = function($track) {
        $track.addClass('playing');
        $track.find('i.fa').attr('class', 'fa fa-pause');
        $curTimer.html(getCurTrackTime());
    };
    var applyStopStyles = function($track) {
        $track.removeClass('playing');
        $track.find('i.fa').attr('class', 'fa fa-play');
    };
    var applyPauseStyles = function($track) {
        $track.find('i.fa').attr('class', 'fa fa-play');
    };
    var pauseTrack = function($track) {
        applyPauseStyles($track);
        smoothPause(1);
        clearInterval(progBarUpdateTimer);
        isPlaying = false;
    };
    var playCurrentTrack = function() {
        applyPlayStyles($curTrack);
        smoothPlay(1);
        progBarUpdateTimer = setInterval(updateProgBar, 100);
        isPlaying = true;
    };
    var changeTrack = function($newTrack, newTrackId) {
        if (curTrack != undefined) {
            applyStopStyles($curTrack);
            smoothPause(0.1);
            resetProgBar();
        }
        setTimeout(function() {
            curTrackIndex = newTrackId.split('track')[1];
            $curTrack = $newTrack;
            $curProgBar = $curTrack.find('.progressBar');
            if ($curTimer != undefined) {
                $curTimer.html('');
            }
            $curTimer = $curTrack.find('.timer');
            curTrackId = newTrackId;
            var src = tracks[curTrackIndex].url;
            if (curTrack == undefined) {
                curTrack = getAudio(src);
            }
            else {
                curTrack.src = src;
            }
            if (trackListType != 'history') {
                $.get('/pushToHistory', {track_url: src});
            }
            applyPlayStyles($curTrack);
            smoothPlay(1);
            progBarUpdateTimer = setInterval(updateProgBar, 100);
            isPlaying = true;
        }, 100);
    };
    var playNextInList = function() {
        curTrackIndex = (parseInt(curTrackIndex) + 1) % tracks.length;
        var newTrackId = 'track' + curTrackIndex;
        changeTrack($('#' + newTrackId), newTrackId);
    };
    var updateProgBar = function() {
        var newWidth = $curTrack.width() * curTrack.currentTime / curTrack.duration;
        $curProgBar.css('width', newWidth + "px");
        if (newWidth === curProgBarWidth) {
            playNextInList();
        }
        else {
            curProgBarWidth = newWidth;
        }
    };
    var resetProgBar = function() {
        clearInterval(progBarUpdateTimer);
        $curProgBar.css('width', 0);
    };
    var makeVolLowTimer,
        makeVolHighTimer;
    var smoothPause = function(sec) {
        var interval = sec * 20;
        clearInterval(makeVolHighTimer);
        makeVolLowTimer = setInterval(function() {
            if (curTrack.volume <= 0.02) {
                curTrack.pause();
                clearInterval(makeVolLowTimer);
            }
            else {
                curTrack.volume -= 0.02;
            }
        }, interval);
    };
    var smoothPlay = function(sec) {
        var interval = sec * 20;
        clearInterval(makeVolLowTimer);
        curTrack.volume = 0;
        curTrack.play();
        // финты с Date — фикс ситуации когда вкладка теряет фокус и setInterval тормозит
        // спасибо, stackoverflow
        var beforeTime = new Date().getTime();
        makeVolHighTimer = setInterval(function() {
            if (curTrack.volume >= 0.99) {
                clearInterval(makeVolHighTimer);
            }
            else {
                var elapsedTime = new Date().getTime() - beforeTime;
                if (elapsedTime > interval) {
                    curTrack.volume += 0.01 * elapsedTime / interval;
                }
                else {
                    curTrack.volume += 0.01;
                }
            }
            beforeTime = new Date().getTime();
        }, interval);
    };
    var getCurTrackTime = function() {
        var timeInSeconds = curTrack.currentTime.toFixed(),
            minutes = Math.floor(timeInSeconds / 60),
            seconds = timeInSeconds - (minutes * 60);
        return minutes + ":" + (seconds < 10 ? ("0" + seconds) : seconds);
    };

    $tracks.click(function(e) {
        if (e.which === 1) {
            var newTrackId = $(this).attr('id');
            if (isPlaying) {
                if (newTrackId === curTrackId) {
                    pauseTrack($(this));
                }
                else {
                    changeTrack($(this), newTrackId);
                }
            }
            else {
                if (newTrackId != curTrackId) {
                    changeTrack($(this), newTrackId);
                }
                else {
                    playCurrentTrack();
                }
            }
        }
    });
});