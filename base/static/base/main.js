$( document ).ready(function() {

    $('.log-out-btn').on('click', function() {
      $.ajax({
        url: "/logout",
        success: function(data) {
          alert("OMG SUCCESS LOGOUG")
          document.location.reload(true);
        },
        error: function(data) {
          alert("OMG ERROR")
        }
      });

    });
});
