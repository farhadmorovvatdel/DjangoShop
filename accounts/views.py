from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect,get_object_or_404
from django.http import  JsonResponse
from django.contrib.auth.views import PasswordResetView,\
    PasswordResetDoneView,\
    PasswordResetConfirmView,PasswordResetCompleteView
from django.urls import reverse_lazy
from django.forms import ValidationError
from django.views import View
from .models import UserProfile
from django.views.decorators.http import require_POST

from django.contrib.auth import  logout,login
from .models import UserProfile

from django.contrib.auth.mixins import LoginRequiredMixin

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
      print(user)
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




@require_POST
def UpdateProfilePictureView(request):
    if request.user.is_authenticated:

      picture=request.FILES.get('user_profile')
      print(picture)
      user=UserProfile.objects.filter(email=request.user.email)
      user.update(UserAvatar=picture)


      return redirect('accounts:userprofile')

    return  render(request,'accounts/Profile.html')

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
         first_name=firstname,last_name=lastname,PhoneNumber=phonenumber,Address=address,
        )

        return redirect('accounts:userprofile')



    return  render(request,'accounts/Profile.html',{'userprofile':userprofile})




class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class UserPaswwordResetDone(PasswordResetDoneView):
    template_name = 'accounts/password_reset_don.html'


class UserPasswordResetConfirm(PasswordResetConfirmView):
    template_name ='accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetComplete(PasswordResetCompleteView):
     template_name = 'accounts/password_reset_complete.html'


class UpdateUserPassword(LoginRequiredMixin,View):

    def get(self,request):
        return render(request,'accounts/ٍedit_user_password.html')

    def post(self,request):
        user = UserProfile.objects.filter(email__iexact=self.request.user.email).first()
        raw_password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if user.check_password(raw_password):
            if confirm_password == new_password:
                user.set_password(new_password)
                user.save()
                logout(request)
                return redirect('Home:home')
            elif new_password != confirm_password:
                context={
                    'newpassword_error':'رمز های عبور با هم مغایرت دارند'
                }
                return render(request,'accounts/ٍedit_user_password.html',context)

        else:
            context = {
                'password_error': 'رمز عبور فعلی صحیح نمی باشد'
            }
            return render(request, 'accounts/ٍedit_user_password.html',context)
        return render(request, 'accounts/ٍedit_user_password.html')