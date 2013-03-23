jQuery(document).ready(function($) {
    $('.event-item').click(function() {
        
        $desc = $(this).children('.event-description').first();
        
        $('.event-description').not($desc).slideUp();
        
        if($desc.text().length > 0) {
            $desc.slideDown();
        }
        
    });
});