$(document).ready(function () {
    $("#options").hide();
    $("#loading").hide();
    $("#display").hide();
    $("#options-button").click(function (event) {
        event.preventDefault();
        $("#options").slideDown();
        $("#names").val('William Riker, Klingon Captain, "Q"');
        $("#locations").val("Sick Bay, Bridge, Engineering");
        $("#scene").val("There is an unknown vessel approaching.");
    });
    $("#submit-button").click(function(event) {
        event.preventDefault();
        $("#start").hide();
        $("#loading").show();
        $.ajax({
            url: "/process",
            type: "POST",
            dataType: "json",
            data: {
                names: $("#names").val(),
                locations: $("#locations").val(),
                settings: $("#settings").val(),
                series: $("#series").val(),
                length: $("#length").val()
            },
            beforeSend: function(xhr){
                xhr.setRequestHeader('X-CSRFToken', csrf)
            },
            error: function(error) {
                if (error.status == 200) {
                $('#display').html(error.responseText);
                $("#loading").hide();
                $("#display").show();
                }
                else{
                $('#display').text('Something Went Wrong.');
                console.log(error)
                $("#loading").hide();
                $("#display").show();
                }
            }
        });
    });
})

