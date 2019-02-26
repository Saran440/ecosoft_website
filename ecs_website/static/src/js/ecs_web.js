$(document).ready(function(){
    $("#oneday").click(function(){
        $("#main_training").hide("fast");
        $("#oneday_training").show("fast");
        $("#twoday_training").hide("fast");
        $("#threeday_training").hide("fast");
    });
    $("#twoday").click(function(){
        $("#main_training").hide("fast");
        $("#oneday_training").hide("fast");
        $("#twoday_training").show("fast");
        $("#threeday_training").hide("fast");
    });
    $("#threeday").click(function(){
        $("#main_training").hide("fast");
        $("#oneday_training").hide("fast");
        $("#twoday_training").hide("fast");
        $("#threeday_training").show("fast");
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
