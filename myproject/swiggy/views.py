from django.shortcuts import render

# Create your views here.
def swiggy(request):
    return render(request, 'home.html')

def swiggy2(request):
    return render(request, 'swiggy2.html')
    