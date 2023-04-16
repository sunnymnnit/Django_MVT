from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,"index.html")
def service(request):
    return render(request,"service.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def career(request):
    return render(request,"career.html")