$(document).ready(function () {
  /////////////////////////////// Email Validation
  function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
  };
  //////////////////////////////////// if user email allready exist
  $('input[type="email"]').keyup(function () {
    const email = $(this).val()
    $('.error small ').remove();
    if (isEmail(email)) {
      $.get("../../ajax/validate_username",
        {
          email: email,
        },
        function (response, status) {
          if (response === 'True') {
            console.log('email registred');
            $('.error small ').remove();
          } else {
            console.log('email Not registred');
            $('.error small ').remove();
            $('.error').prepend('<small class="text-danger">Email not registred</small>');          
          }
        });
    }
  });

});