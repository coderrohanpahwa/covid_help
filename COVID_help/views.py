from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.
def index(request):
    return render(request,'COVID_help/index.html')
def about(request):
    return render(request, 'COVID_help/about.html')
def info(request):
    name=request.POST.get('name','abc')
    Locality=request.POST.get('Locality','abc')
    address=request.POST.get('address','abc')
    name_suf=request.POST.get('name_suf','abc')
    name_phn=request.POST.get('name_phn','abc')
    contact = Contact(name=name, Locality=Locality,address=address, name_suf=name_suf,name_phn=name_phn)
    contact.save()

    return HttpResponse("You have successfully submitted details. We will get you back as soon as possible.")