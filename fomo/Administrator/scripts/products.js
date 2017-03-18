$(function(){

  console.log("Hey");
  $('.update_button').click(function(){
    // console.log($(this));
    var pid = $(this).attr('data-pid'); //"this" means whatever you click on
    console.log(pid)
    //get the product id

    //add the server for the current qty

    $(this).siblings('.quantity-container').load('/Administrator/products.get_quantity/' + pid);

  });



//MODAL
  $('.delete_link').click(function(event){
    //don't do the normal behavior
    event.preventDefault();

    //Grab the href from the html
    console.log(this);
    var link = $(this).attr('href');
    console.log(link);

    //Grab
    $('#for-real').attr('href', link);
    //Show popup
    $('#myModal').modal();

  });

});
