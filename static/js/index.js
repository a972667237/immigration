$(document).ready(function(){
  new WOW().init();
  $.fatNav();

  $(".card").hover(function(){

    if($(this).hasClass("pulse")){
      $(this).removeClass("pulse");
      $(this).css("animation-name", "none");

    }
    else{
      $(this).css("animation-name", "pulse");
      $(this).addClass("pulse animated");
    }
  });
});