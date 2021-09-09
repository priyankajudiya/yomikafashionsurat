$(document).ready(function () {

  var username = false
  var password = false
  var first_name = false
  var last_name = false
  var terms_checked = false
  /////////////////////////////// Email Validation
  function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
  };
  //////////////////////////////////// if user email allready exist

  $('input[type="email"]').keyup(function () {
    const email = $(this).val()
    if (isEmail(email)) {
      $.get("../../ajax/validate_username",
        {
          email: email,
        },
        function (response, status) {
          if (response === 'True') {
            $('.error small').remove();
            $('.error').prepend('<small class="text-danger animate__animated animate__fadeIn animate__repeat-3"><b>email address already registred</b></small>');
            $('#Email').addClass('animate__animated animate__heartBeat text-danger animate__infinite');
            $('input[type="email"]').attr('autocomplete', 'off');
            username = false
          } else {
            $('.error small').remove();
            $('#Email').removeClass('animate__animated animate__heartBeat animate__infinite text-danger');
            $('input[type="email"]').removeAttr('autocomplete');
            $('input[type="email"]').css("background-color", "");
            username = true
          }

          $('input[type="email"]').blur(function () {
            if (response === 'True') {
              $('input[type="email"]').css("background-color", "#f8a488");
            } else {
              $('input[type="email"]').css("background-color", "");
            }
          });

        });
    }
  });

  ////////////////////////// password validation
  var pass = '0'
  var pass1 = '0'
  /////////// Pass
  $('input[name="password"]').keyup(function () {
    pass = $(this).val();

    if (pass.length < 6) {
      $('#pass p').remove();
      $('#pass').prepend('<p class="text-danger">password must be 6-12 characters </p>');
    } else {
      $('#pass p').remove();
      $('input[name="password"]').removeAttr('style');
    }

    if (pass.length === 0) {
      $('#pass p').remove();
    }

    if (pass1.length > 1 && pass != pass1) {
      password = false
      $('#pass1 p').remove();
      $('#pass1').prepend('<p class="text-danger">password not match</p>');
    } else {
      password = true
    }
  });

  $('input[name="password"]').blur(function () {
    if (pass.length < 6) {
      $('input[name="password"]').attr('style', 'background-color:#f8a488;');
    } else {
      $('input[name="password"]').removeAttr('style');
    }
  });

  ////////// Pass1
  $('input[name="password1"]').keyup(function () {
    pass1 = $(this).val()

    if (pass != pass1) {
      $('#pass1 p').remove();
      $('#pass1').prepend('<p class="text-danger">password not match</p>');
      password = false
    } else {
      $('#pass1 p').remove();
      $('input[name="password1"]').removeAttr('style');
      password = true
    }

    if (pass1.length === 0) {
      $('#pass1 p').remove();
    }
  });

  $('input[name="password1"]').blur(function () {
    if (pass !== pass1) {
      $('input[name="password1"]').attr('style', 'background-color:#f8a488;');
    } else {
      $('input[name="password1"]').removeAttr('style');
    }
  });

  $('input[name="first_name"]').keyup(function () {
    const fname = $(this).val()
    if (fname.length > 0) {
      first_name = true
    } else {
      first_name = false
    }
  });

  $('input[name="last_name"]').keyup(function () {
    const lname = $(this).val()
    if (lname.length > 0) {
      last_name = true
    } else {
      lastname = false
    }
  });

  ////////////// if form filled
  $('body').hover(function () {
    if (username && password && first_name && last_name) {
      $('input').removeAttr('required');
    } else {
      $('input').attr('required', 'required');
      $('#cb2').removeAttr('required');
    }
  });

  ///////////////////////// Terms Checkbox
  $('#cb1').click(function () {
    if ($(this).prop("checked") == true) {
      $('label[for="cb1"]').removeClass('text-danger');
      terms_checked = true
    }
    else if ($(this).prop("checked") == false) {
      $('label[for="cb1"]').addClass('text-danger');
      terms_checked = false
    }
  });
 
  //////////////////// on Submit
  $('input[type="submit"]').click(function (event) {

    if (username && password && first_name && last_name && terms_checked) {
      event.preventDefault(None);
    } else {
      event.preventDefault();
      $('label[for="cb1"]').addClass('text-danger');
      $('label[for="cb1"]').attr('style','font-size:16px; font-weight: 900;');

      if (username && password && first_name && last_name && !terms_checked){
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Read Terms and Conditions',
          // footer: '<a href>Why do I have this issue?</a>'
        });
      }else{
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'All fiealds are required',
          // footer: '<a href>Why do I have this issue?</a>'
        });
      }
    }
  });


});