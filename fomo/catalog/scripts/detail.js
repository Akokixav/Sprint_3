$(function(){

var urlArray = window.location.pathname.split('/');
var pid = urlArray[3];


$('#picturemodal').click(function(){
    $.loadmodal('/catalog/detail.modal/' + pid);

  });



});
