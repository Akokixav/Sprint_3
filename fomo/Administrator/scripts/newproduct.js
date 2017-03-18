// function(){
//   console.log("Hey I'm ready");
// }
// console.log('Hello world');
//
// var contacttype2 = $('#id_contacttype');
// contacttype2.addClass('HelloClass') This will add a class to the object
// console.log(contacttype2)
//
// console.log('Hello world')
// def $()

$(function(){

var producttype = $('#id_producttype');
var value = producttype.val();
  // $('.producttype-quantity').closest('p').hide();


$('#id_producttype').change(function(event){
  var value = producttype.val();

  if (value == 'bulk'){
    $('.producttype-quantity').closest('p').show(500);
    $('.producttype-rp').closest('p').show(500);
    $('.producttype-rq').closest('p').show(500);


  } else {
    $('.producttype-quantity').closest('p').hide(500);
    $('.producttype-rp').closest('p').hide(500);
    $('.producttype-rq').closest('p').hide(500);
  }





  console.log(value);

});
producttype.change();


});
