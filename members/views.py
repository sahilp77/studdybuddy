from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# Create your views here.
def Members(request):
    member = Member.objects.all()
    context = {"member": member}
    
    return render(request,"members/all_members.html",context)
