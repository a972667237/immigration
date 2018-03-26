$(document).ready(function(){
    function disappear(that){
        $(that).addClass("disappear");
        $(that).parent().parent().children(".panel-block").animate({height: "0", padding: "0"});
    }
    function show(that){
        $(that).removeClass("disappear");
        $(that).parent().parent().children(".panel-block").animate({height: $(that).parent().parent().children(".panel-block").data("height") + "px", padding: "0.5em 0.75em"});
    }

    $(".panel-block").each(
        function(index){
            $(this).data("height", $(this).height());
            if(index != 0){
                disappear($(this).parent().children(".panel-heading").children("a"));
            }
        }
    );



    $(".panel-heading a").click(function(){
        let that = this;
        if($(this).hasClass("disappear")){
            $(".panel-heading a").each(function(){
                if(that != this)
                    disappear(this);
            });
            show(this);
        }
        else{
            disappear(this);
        }
    });
});