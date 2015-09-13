$(document).ready(function() {

  $('button').on('click', function() {
    this.blur();
  });

  $('.find-court-btn').on('click', function() {
    $('.court-list').toggleClass('hidden');
  })

  setTimeout(function() {
    $('.messages').hide();
  }, 3000);

  var allnum = $('.green');
  var values = [];

  for (var i = 0; i < allnum.length; i++) {
    values.push(parseInt($(allnum[i]).text()));
  }

  for (var i = 0; i <= values[0]; i++) {
    (function(e) {
      setTimeout(function() {
        $(allnum[0]).text(e);
    }, (1000 / values[0]) * e);
    })(i);
  }

  for (var i = 0; i <= values[1]; i++) {
    (function(e) {
      setTimeout(function() {
        $(allnum[1]).text(e);
    }, (1000 / values[1]) * e);
    })(i);
  }

  for (var i = 0; i <= values[2]; i++) {
    (function(e) {
      setTimeout(function() {
        $(allnum[2]).text(e);
    }, (1000 / values[2]) * e);
    })(i);
  }

  for (var i = 0; i <= values[3]; i++) {
    (function(e) {
      setTimeout(function() {
        $(allnum[3]).text(e);
    }, (1000 / values[3]) * e);
    })(i);
  }

  for (var i = 0; i <= values[4]; i++) {
    (function(e) {
      setTimeout(function() {
        $(allnum[4]).text(e);
    }, (1000 / values[4]) * e);
    })(i);
  }
});
