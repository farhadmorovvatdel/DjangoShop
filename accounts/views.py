from django.shortcuts import render,redirect
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import  messages
from django.views import View

from .models import UserProfile
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods
from django.contrib.auth import  logout,login
from .models import UserProfile

@require_POST
def UserRegister(request):
    email=request.POST["email"]
    password=request.POST["password"]
    is_exists=UserProfile.objects.filter(email=email).exists()
    if is_exists :
        return JsonResponse({
            'status':'duplicate'
        })
    else:
     user=UserProfile.objects.create(email=email,is_active=True)
     user.set_password(password)
     user.save()
     return JsonResponse({
         'status':'ok'
     })

def UserLogin(request):
    if request.method == "POST":
      email = request.POST["email"]
      raw_password = request.POST["password"]
      user=UserProfile.objects.filter(email=email).first()
      if user is not  None:
          is_correctpassword=user.check_password(raw_password)
          if is_correctpassword:
              login(request,user)
          else:
              return JsonResponse(
                  {
                      'status':'notfound'
                  }
              )

    return  render(request,'Home/Index.html')


def UserLogout(request):
    logout(request)
    return  redirect('Home:home')


@require_http_methods(['GET','POST'])
def UserProfileView(request):
    if request.user.is_authenticated:
        userprofile=UserProfile.objects.filter(email__iexact=request.user.email).first()
    else:
        return redirect('accounts:userlogin')
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        address=request.POST.get('address')
        userprofile = UserProfile.objects.filter(email__iexact=request.user.email).update(
         first_name=firstname,last_name=lastname,email=email,PhoneNumber=phonenumber,Address=address
        )

        return redirect('accounts:userprofile')



    return  render(request,'accounts/Profile.html',{'userprofile':userprofile})








