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

  // var allnum = $('.green');
  // var values = [];
  //
  // for (var i = 0; i < allnum.length; i++) {
  //   values.push(parseInt($(allnum[i]).text()));
  // }
  //
  // for (var i = 0; i <= values[0]; i++) {
  //   console.log(values[0]);
  //   (function(e) {
  //     setTimeout(function() {
  //       $(allnum[0]).text(e);
  //   }, 90 * e);
  //   })(i);
  // }
  //
  // for (var i = 0; i <= values[1]; i++) {
  //   console.log(values[1]);
  //   (function(e) {
  //     setTimeout(function() {
  //       $(allnum[1]).text(e);
  //   }, 90 * e);
  //   })(i);
  // }
  //
  // for (var i = 0; i <= values[2]; i++) {
  //   console.log(values[2]);
  //   (function(e) {
  //     setTimeout(function() {
  //       $(allnum[2]).text(e);
  //   }, 90 * e);
  //   })(i);
  // }
  //
  // for (var i = 0; i <= values[3]; i++) {
  //   console.log(values[3]);
  //   (function(e) {
  //     setTimeout(function() {
  //       $(allnum[3]).text(e);
  //   }, 90 * e);
  //   })(i);
  // }
  //
  // for (var i = 0; i <= values[4]; i++) {
  //   console.log(values[4]);
  //   (function(e) {
  //     setTimeout(function() {
  //       $(allnum[4]).text(e);
  //   }, 90 * e);
  //   })(i);
  // }
});
