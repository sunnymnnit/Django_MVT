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
def feature(request):
    return render(request,"feature.html")
def centre(request):
    return render(request,"centre.html")
def pricing(request):
    return render(request,"pricing.html")
def form(request):
    return render(request,"form.html")
def orderForm(request):
    return render(request,"orderForm.html")
def myCustomForm(request):
    return render(request,"myCustomForm.html")