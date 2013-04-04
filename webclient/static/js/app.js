jQuery(document).ready(function($) {
    $('.event-item').click(function() {
        
        $desc = $(this).children('.event-description').first();
        
        if($desc.text().length == 0) {
            return; // no text to show
        }
        
        $('.event-description').not($desc).slideUp();
        
        if($desc.text().length > 0) {
            $desc.slideDown();
        }
        
    });
    
    
    $('.news-list > li').click(function() {
        
    });
    
    
    function updateClock() {
        // show and update clock
        var now = new Date();
        var hours = now.getHours();
        var minutes = now.getMinutes();
        
        function formatTime(i) {
            if(i < 10) {
                i = "0" + i;
            }
            
            return i;
        }
        
        var timeString = hours + ":" + minutes;
        console.log(timeString);
    }
    
    updateClock();
    setInterval(updateClock, 1000);
    
});
