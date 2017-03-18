$(function() {
    // update the time every 1 seconds
    window.setInterval(function() {
        $('.browser-time').text('The current browser time is ' + new Date() + '.');
    }, 1000);

    console.log($.loadmodal);

$('#modallogin_button').click(function(){
  $.loadmodal('/account/login_class.modal');



});

$('#landing').click(function(){
  window.location.href = "www.google.com"
});

});
