from django.shortcuts import render

def loginpage(request):
    return render(request, 'home.html')
