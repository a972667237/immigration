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
  $(".is-link").click(function() {
      var params1 = $("form").serialize();
      $.ajax( {
        type : "POST",
        url : "/info",
        data : params1,
        success : function(msg) {
            alert(msg);
            $("input").val("");
            $("textarea").val("");
        }
    });
  })
});
