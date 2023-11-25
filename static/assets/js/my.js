$(document).ready(function() {
    $('#categoryid').change(function(e) {
        e.preventDefault();
        var selectoption = $('#categoryid').val();
        alert(selectoption)
        $.ajax({
            type:'GET',
            data: {
                "option_name":selectoption
            },
            url:'products/productcategory'
        })
    });
});
function UserRegister() {
    $('#registerform').on('submit', function (e) {
        e.preventDefault()
        if ($('#registeremail').val() === '') {
            Swal.fire({
                icon: 'error',
                title: 'توجه',
                text: 'برای ثبت نام لطفا ایمیل خود را وارد کنید ',
                timer: 2000


            })
        } else if ($('#registerpassword').val() === '') {
            Swal.fire({
                icon: 'error',
                title: 'توجه',
                text: 'برای ثبت نام لطفا رمز خود را وارد کنید ',
                timer: 2000

            })
        } else
            // var form = $(this);
            // var actionUrl = form.attr('action');
            var serializedData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: 'accounts/register',
            data: serializedData,
            success:function (res) {
                if (res.status === 'ok') {
                    Swal.fire({
                        position: 'center',
                        icon: 'success',
                        title: 'ثبت نام شما با موفقیت انجام شد',
                        showConfirmButton: false,
                        timer: 1500

                    })
                    $(location).attr('href', 'accounts/userprofile');
                } else
                    Swal.fire({
                        icon: 'error',
                        title: 'توجه',
                        text: 'کابری با این مشخصات قبلا ثبت نام کرده است',
                        timer: 2000

                    })


            }


        })

    })
}

function UserLogin(){
    $('#loginform').on('submit',function (e){
        e.preventDefault()
        if ($('#loginemail').val() === '') {
            Swal.fire({
                icon: 'error',
                title: 'توجه',
                text: 'برای ورود لطفا ایمیل خود را وارد کنید ',
                timer: 2000


            })
        }
            else if ($('#loginpassword').val() === '') {
            Swal.fire({
                icon: 'error',
                title: 'توجه',
                text: 'برای ورود لطفا رمز خود را وارد کنید ',
                timer: 2000

            })
        }
            else
                var serializedData = $(this).serialize();

                $.ajax({
                type: 'POST',
                url: 'accounts/login',
                data: serializedData,
                success:function (res) {
                    if (res.status === 'notfound') {

                        Swal.fire({
                            icon: 'error',
                            title: 'توجه',
                            text: ' نام کاربری یا رمز عبور اشتباه می باشد',
                            timer: 2000

                        })
                    } else

                     $(location).attr('href','accounts/userprofile');



                }
            })
        }
    )
}
function UserProfileUpdate() {
    $('#profileform').on('submit', function (e) {
        e.preventDefault()
        var serializedData = $(this).serialize();
        var url= $('#profileform').attr('action')
        $.ajax({
            type:'POST',
            url:url,
            data:serializedData,
            success:function (res){
      Swal.fire({
      position: 'center',
      icon: 'success',
      title: 'اطلاعات شما با موفقیت ثبت شد',
      showConfirmButton: false,
      timer: 1500

            })


            }

        })

    })
}
function UserProfilePicture(){
    data=$('#user_profile').val()
}