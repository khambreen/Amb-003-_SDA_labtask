from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("This page is related to home")
    return render(request, 'home.html')
   
def about(request):
    #return HttpResponse("This page is related to about")
    return render(request, 'about.html')
def contact(request):
    #return HttpResponse("This page is related to contact")
    return render(request, 'contact.html')
def projects(request):
    #return HttpResponse("This page is related to projects")
    return render(request, 'projects.html')
