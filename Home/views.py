from django.shortcuts import render

def Home(request):
    return  render(request,"Home/Index.html")

def Header(request):
    return render(request,"shared/Header.html")


def Footer(request):
    return  render(request,"shared/Footer.html")
