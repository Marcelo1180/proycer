from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("holas")
    return render(request, 'home.html')