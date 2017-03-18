$(function(){

  console.log('Hello Ni hao')
  $('#form_container > form').ajaxForm({
    target:'#jquery-loadmodal-js-body'
  });

  var images = $('#jquery-loadmodal-js-body img');
  var current_image_num = 0;

  function showPic(pnum){
    //Hide all images
    images.hide();
    //Show only the current image
    var current = $(images[current_image_num]);
    current.show();
  }

  //Show only the first picture on image load
  showPic(current_image_num)

  //Button events
  $('#next_pic_button').click(function(){
    current_image_num++;
    if (current_image_num == images.length){
      current_image_num = 0;
    }
    showPic();
  }); //Click

  $('#previous_pic_button').click(function(){
    current_image_num--;
    
    showPic();
  }); //Click

});
