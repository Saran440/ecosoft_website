$(document).ready(function(){
    $("#oneday").click(function(){
        $("#main_training").hide();
        $("#oneday_training").show();
        $("#twoday_training").hide();
        $("#threeday_training").hide();
        $("html, body").animate({scrollTop: 0}, 100);
    });
    $("#twoday").click(function(){
        $("#main_training").hide();
        $("#oneday_training").hide();
        $("#twoday_training").show();
        $("#threeday_training").hide();
        $("html, body").animate({scrollTop: 0}, 100);
    });
    $("#threeday").click(function(){
        $("#main_training").hide();
        $("#oneday_training").hide();
        $("#twoday_training").hide();
        $("#threeday_training").show();
        $("html, body").animate({scrollTop: 0}, 100);
    });
    $('#contact_email').keyup(function() {
       if($(this).val() != '') {
          $('#subscribe').prop('disabled', false);
       }
       else {
          $('#subscribe').prop('disabled', true);
       }
    });
    $("#subscribe").click(function(){
        alert("Thank you for subscribe.");
    });
});
