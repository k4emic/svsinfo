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
    setInterval(updateClock, 1000);
    
});
