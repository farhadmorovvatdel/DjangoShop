from django.urls import path
from .views import UserProfileView,UserRegister,UserLogout,UserLogin
app_name='accounts'
urlpatterns=[

    path("login",UserLogin,name='userlogin'),
    path("register",UserRegister,name='userregister'),
    # path("show_user_profile",show_user_profile,name="show_user_profile"),
    path("logout",UserLogout,name='logout'),
    path("userprofile", UserProfileView, name='userprofile'),
]