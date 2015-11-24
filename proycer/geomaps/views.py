from django.shortcuts import render, HttpResponse, RequestContext, HttpResponseRedirect


# Create your views here.
def home(request):
    # return HttpResponse("holas")
    return render(request, 'home.html')
    # return render(request, 'index.html')