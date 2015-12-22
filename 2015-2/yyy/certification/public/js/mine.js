function getToken() {
    var email =  $("#email").val();
    $.ajax({

        method: "GET",
        url:"http://www.certification.com:8888/mail/send?email="+email,
        success: function (data) {
            console.log(data);
            $('#res').text(data);
        },
        error:function( err ) {
            console.info( JSON.stringify(err));
        }

    });


};