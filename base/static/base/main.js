$( document ).ready(function() {

    $('button').on('click', function() {
        this.blur();
    });

    $('.find-court-btn').on('click', function() {
        $('.court-list').toggleClass('hidden');
    })

    setTimeout(function(){
         $('.messages').hide();
    }, 3000);

});
