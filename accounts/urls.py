from django.urls import path
from .views import UserProfileView,UserRegister,UserLogout,UserLogin\
    ,UserPasswordResetView,UserPaswwordResetDone,UserPasswordResetConfirm,\
    UserPasswordResetComplete,UpdateUserPassword,UpdateProfilePictureView


app_name='accounts'
urlpatterns=[
    path("login",UserLogin,name='userlogin'),
    path("register",UserRegister,name='userregister'),
    # path("show_user_profile",show_user_profile,name="show_user_profile"),
    path("logout",UserLogout,name='logout'),
    path("userprofile", UserProfileView, name='userprofile'),
    path("updateprofile", UpdateProfilePictureView, name='userprofilepicture'),
    path("password-reset/",UserPasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/',UserPaswwordResetDone.as_view(),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',UserPasswordResetConfirm.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',UserPasswordResetComplete.as_view(),name='password_reset_complete'),
    path('password-update/',UpdateUserPassword.as_view(),name='update_user_password'),



]