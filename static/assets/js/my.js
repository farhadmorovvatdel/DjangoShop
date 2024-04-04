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
        if ($('#firstname').val()===''){
             Swal.fire({
                icon: 'error',
                title: 'توجه',
                text: 'نام کاربری نمی تواند خالی باشد',
                timer: 2000


            })
        }
        else if($('#lastname').val()=== ''){
             Swal.fire({
                icon: 'error',
                title: 'توجه',
                text: 'نام خانوادگی نمی تواند خالی باشد',
                timer: 2000


            })
        }
        else if($('#phonenumber').val()=== ''){
            Swal.fire({
                icon: 'error',
                title: 'توجه',
                text: 'شماره تلفن نمی تواند خالی باشد',
                timer: 2000


            })
        }
        else
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


$(document).ready(function (){
    $(".price").change(function (){
        var valve=$(this).value()
        alert(valve)
    })
})
//
$(document).ready(function() {
    $(".mycat").change(function () {


        var catname= $(this).val()

        // var id = $(this).children(":selected").attr("id")
        // var url = '/products/filter/'+id
        // alert(url)
        $.ajax({
            url:'/products/filter/'+ catname,
            type:'GET',
            data:{cat_name:catname},
            success:function (data) {
                 // $('.e-procategory-box').html('<pre>'+ JSON.stringify(data,null,2)+'</pre>')
//                 $('#filterproducts').empty()
//                 $('#filterproducts').html(JSON.stringify(data))
//                 $.each(data, function(index, item) {
//     $('#filterproducts').append('<div>' + JSON.stringify(item) + '</div>');
//      console.log(item.title)
// });
 $('.e-procategory-box').empty()
                $.each(data, function (index, item) {

                    $('#listfilter').append('<div class="e-procategory-box" id="listfilter">\n' +
                        '            <div class="procategory-gridbox">\n' +
                        '                <div class="c-product-box">\n' +
                        '                    <div class="na-top-sec text-center">\n' +
                        '                        <div class="na-imgbox">\n' +
                        '                            <div class="na-mainimg">\n' +
                        '                                {% if i.image %}\n' +
                        '                                    <img src="{{ i.image.url }}" alt="product-img" class="img-fluid">\n' +
                        '                                {% endif %}\n' +
                        '                            </div>\n' +
                        '                            {% if i.image %}\n' +
                        '                                <div class="na-overlay-img">\n' +
                        '                                    <img src="{{i.image.url}}" alt="product-img" class="img-fluid">\n' +
                        '                                </div>\n' +
                        '                            {% endif %}\n' +
                        '                        </div>\n' +
                        '                        <div class="na-color-details">\n' +
                        '                            <h2 class="na-color-title">رنگ های موجود </h2>\n' +
                        '                            <ul class="na-color-skin">\n' +
                        '                                <li></li>\n' +
                        '                                <li></li>\n' +
                        '                                <li></li>\n' +
                        '                                <li></li>\n' +
                        '                                <li></li>\n' +
                        '                            </ul>\n' +
                        '                        </div>\n' +
                        '                        <ul class="na-hover-content na-vartical-hover">\n' +
                        '                            <li><a href="wishlist.html"><span><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="16px" height="15px"><path fill-rule="evenodd" fill="rgb(242, 243, 245)" d="M14.692,1.994 C13.881,1.077 12.769,0.571 11.560,0.571 C10.652,0.571 9.819,0.871 9.087,1.461 C8.846,1.656 8.618,1.882 8.406,2.135 C8.198,1.884 7.968,1.658 7.725,1.461 C6.994,0.871 6.161,0.571 5.253,0.571 C4.044,0.571 2.932,1.077 2.121,1.994 C1.329,2.891 0.892,4.113 0.892,5.433 C0.892,6.786 1.368,8.018 2.392,9.308 C3.276,10.421 4.528,11.534 5.988,12.834 C6.452,13.246 7.027,13.759 7.610,14.290 C7.830,14.491 8.113,14.602 8.406,14.602 C8.700,14.602 8.983,14.491 9.202,14.290 C9.788,13.756 10.364,13.244 10.828,12.831 C12.279,11.540 13.532,10.426 14.420,9.308 C15.444,8.018 15.921,6.787 15.921,5.433 C15.921,4.113 15.484,2.891 14.692,1.994 ZM5.253,2.201 C5.803,2.201 6.310,2.385 6.760,2.747 C7.173,3.082 7.464,3.509 7.636,3.809 C7.799,4.094 8.087,4.264 8.406,4.264 C8.725,4.264 9.014,4.094 9.177,3.809 C9.348,3.510 9.638,3.083 10.053,2.747 C10.502,2.385 11.009,2.201 11.560,2.201 C12.322,2.201 13.023,2.518 13.532,3.095 C14.059,3.691 14.348,4.521 14.348,5.433 C14.348,6.401 13.996,7.277 13.207,8.272 C12.410,9.275 11.207,10.345 9.804,11.594 L9.776,11.619 C9.401,11.952 8.914,12.386 8.405,12.845 C7.915,12.400 7.445,11.982 7.005,11.591 C5.610,10.349 4.405,9.277 3.606,8.272 C2.817,7.277 2.464,6.401 2.464,5.433 C2.464,4.521 2.754,3.691 3.281,3.095 C3.790,2.518 4.490,2.201 5.253,2.201 Z"/></svg></span></a></li>\n' +
                        '                            <li><a href="cart.html"><span><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="16px" height="17px"><path fill-rule="evenodd" fill="rgb(255, 255, 255)" d="M15.021,2.851 C14.062,4.907 13.088,6.956 12.135,9.016 C11.930,9.458 11.634,9.640 11.181,9.638 C9.373,9.629 7.565,9.635 5.757,9.637 C5.596,9.637 5.434,9.629 5.275,9.650 C4.902,9.700 4.643,10.009 4.629,10.400 C4.615,10.804 4.874,11.151 5.255,11.214 C5.412,11.241 5.575,11.236 5.735,11.236 C8.012,11.238 10.289,11.237 12.566,11.238 C13.280,11.238 13.632,11.507 13.625,12.038 C13.617,12.573 13.269,12.832 12.558,12.832 C11.379,12.832 10.200,12.832 9.022,12.832 C9.022,12.832 9.022,12.831 9.022,12.831 C7.843,12.831 6.664,12.832 5.486,12.830 C4.381,12.829 3.531,12.194 3.224,11.143 C2.919,10.097 3.284,9.038 4.194,8.393 C4.374,8.265 4.406,8.164 4.343,7.947 C3.774,5.956 3.213,3.963 2.663,1.967 C2.594,1.713 2.490,1.621 2.246,1.631 C1.818,1.650 1.389,1.648 0.961,1.638 C0.441,1.626 0.115,1.295 0.126,0.812 C0.136,0.345 0.452,0.043 0.961,0.036 C1.631,0.028 2.301,0.028 2.970,0.035 C3.519,0.041 3.740,0.225 3.899,0.784 C4.142,1.636 4.142,1.637 4.990,1.637 C7.990,1.636 10.990,1.635 13.991,1.634 C14.124,1.634 14.259,1.631 14.392,1.645 C15.007,1.711 15.298,2.256 15.021,2.851 ZM4.588,3.243 C5.025,4.809 5.443,6.326 5.885,7.835 C5.914,7.933 6.128,8.024 6.256,8.025 C7.690,8.038 9.123,8.024 10.557,8.040 C10.825,8.043 10.960,7.952 11.076,7.699 C11.687,6.366 12.316,5.043 12.937,3.715 C13.004,3.571 13.063,3.422 13.140,3.243 C10.265,3.243 7.454,3.243 4.588,3.243 ZM6.878,14.440 C7.286,14.442 7.619,14.795 7.621,15.226 C7.622,15.658 7.295,16.018 6.891,16.029 C6.458,16.041 6.129,15.689 6.136,15.221 C6.142,14.771 6.458,14.438 6.878,14.440 ZM11.374,14.437 C11.778,14.438 12.117,14.792 12.123,15.222 C12.130,15.668 11.777,16.040 11.357,16.029 C10.943,16.018 10.631,15.670 10.634,15.223 C10.636,14.779 10.959,14.436 11.374,14.437 Z"/></svg></span></a></li>\n' +
                        '                            <li><a href="product_details.html"><span><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="15px" height="16px"><path fill-rule="evenodd" fill="rgb(255, 255, 255)" d="M14.100,13.964 C13.679,13.500 13.249,13.043 12.820,12.586 L10.652,10.282 C12.647,7.194 11.603,3.514 9.448,1.831 C7.146,0.033 4.034,0.263 2.049,2.378 C0.061,4.497 -0.177,7.831 1.484,10.306 C2.306,11.533 3.683,12.418 5.168,12.673 C6.212,12.851 7.786,12.806 9.425,11.601 L9.495,11.684 C9.649,11.868 9.807,12.056 9.973,12.235 C10.891,13.225 11.810,14.213 12.740,15.191 C12.924,15.383 13.145,15.522 13.348,15.571 C13.410,15.585 13.470,15.593 13.530,15.593 C13.825,15.593 14.089,15.415 14.259,15.093 C14.462,14.710 14.404,14.298 14.100,13.964 ZM8.803,3.755 C9.536,4.540 9.938,5.586 9.936,6.701 C9.935,7.812 9.528,8.855 8.791,9.640 C8.056,10.422 7.080,10.853 6.043,10.853 C6.041,10.853 6.038,10.853 6.036,10.853 C4.997,10.851 4.017,10.410 3.275,9.611 C2.539,8.819 2.138,7.779 2.147,6.684 C2.165,4.356 3.878,2.535 6.048,2.535 C6.049,2.535 6.052,2.535 6.053,2.535 C7.094,2.536 8.071,2.969 8.803,3.755 Z"/></svg></span></a></li>\n' +
                        '                        </ul>\n' +
                        '                    </div>\n' +
                        '                    <div class="na-top-heading text-center">\n' +
                        '                        <a href="{{ i.get_absolute_url }}"  class="na-name">{{ i.title}}</a>\n' +
                        '                        <h2 class="na-price"></h2>\n' +
                        '                    </div>\n' +
                        '                </div>\n' +
                        '            </div>\n' +
                        '            <div class="procategory-listbox">\n' +
                        '                <div class="pc-top-heading">\n' +
                        '                    <a href="product_details.html" class="na-name">کت کلاه دار خاکستری مشکی</a>\n' +
                        '                    <h2 class="na-price"> تومان</h2>\n'+
                        '                    <p class="procategory-des">طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردی است.</p>\n' +
                        '                    <div class="pc-color-details">\n' +
                        '                        <h2 class="na-color-title">رنگ های موجود </h2>\n' +
                        '                        <ul class="na-color-skin">\n' +
                        '                            <li></li>\n' +
                        '                            <li></li>\n' +
                        '                            <li></li>\n' +
                        '                            <li></li>\n' +
                        '                            <li></li>\n' +
                        '                        </ul>\n' +
                        '                    </div>\n' +
                        '                </div>\n' +
                        '            </div>\n' +
                        '        </div>'   )

                })
            }
                })
      })
})
