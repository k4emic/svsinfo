jQuery(document).ready(function($) {
    $('.event-item').click(function() {
        $('.event-description').slideUp();
        $desc = $(this).children('.event-description').first();
        if($desc.text().length > 0) {
            $desc.slideDown();
        }
        
    });
});