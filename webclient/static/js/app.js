jQuery(document).ready(function($) {
    $('.event-item').click(function() {
        
        var $elm = $(this).children('.collapse-container').first();
        var has_description = ($elm.children('.event-description').first().text().length > 0);
        var has_news = ($elm.children('.event-news-container').length > 0);
        
        if(!has_description && !has_news) {
            return false;
        }
        
        $('.collapse-container').not($elm).slideUp();
        
        $elm.slideDown();
        
    });
    
    function updateClock() {
        // show and update clock
        var now = new Date();
        var hours = formatTime(now.getHours());
        var minutes = formatTime(now.getMinutes());
        
        function formatTime(i) {
            if(i < 10) {
                i = "0" + i;
            }
            
            return i;
        }
        
        var timeString = hours + ":" + minutes;
        var elm_selector = '#clock';
        $(elm_selector).html(timeString);
        //console.log(timeString);
    }
    
    updateClock();
    
    var last_movement = 0;
    setInterval(idleHandler, 60 * 1000);
    
    $(this).mousemove(function(a, b) {
        last_movement = 0;
    });
    
    function idleHandler() {
        last_movement++;
        //console.log('time since last movement: ' + last_movement);
        
        if(last_movement >= 20) {
            window.location.reload();
        }
    }
    
    $(this).bind("contextmenu", function(e) {
        e.preventDefault();
    });
});
