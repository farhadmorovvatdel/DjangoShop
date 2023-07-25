from django.shortcuts import render,redirect

def Home(request):
    print(request.user.is_authenticated)
    return  render(request,"Home/Index.html")

def Header(request):
    return render(request,"shared/Header.html")


def Footer(request):
    return  render(request,"shared/Footer.html")





