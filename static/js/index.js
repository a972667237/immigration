$(document).ready(function(){
  new WOW().init();
  $.fatNav();
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
  });
});
