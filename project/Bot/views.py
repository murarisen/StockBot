from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is myhompage")

def about(request):
    return render( request,'about.html')

def login(request):
    return render( request, 'login.html')

def market(request):
    return render(request, 'base.html')

def contect(request):
    return HttpResponse("This is contect page")

