from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from .models import takeNotes,contactUs,contactOrg

def index(request):
    arr = []
    params = takeNotes.objects.all() 
    for p in params:
        arr.append(p)
    print(arr)
    print(params)
    return render(request,'index.html',{'params':arr})

def addnote(request):
    note = request.POST.get('note') 
    desc = request.POST.get('desc')
    important=request.POST.get('important','off')
    print(important)
    data = takeNotes(note=note,desc=desc,important=important)
    data.save()
    messages.info(request, "Note added")
    return redirect('/')
def delete(request,id):
    arr1=[]
    params = takeNotes.objects.get(id=id) 
    params.delete()
    messages.info(request, "Note deleted")
    return HttpResponseRedirect(reverse('index'))
def edit(request,id):
    obj = takeNotes.objects.get(id=id)
    params = takeNotes.objects.all()
    context={"obj":obj,"params":params}
    return render(request,'index.html',context)

def update(request,id):
    obj = takeNotes.objects.get(id=id)
    obj.note = request.POST.get('note')
    obj.desc = request.POST.get('desc')
    obj.save()
    messages.info(request, "Note updated")
    return redirect('/')
def contactus(request):
    if request.method == "POST":
        name= request.POST.get('name')
        phonenumber= request.POST.get('phonenumber')
        email= request.POST.get('email')
        issue= request.POST.get('issue')
        obj = contactUs(name=name,phonenumber=phonenumber,email=email,issue=issue)
        obj.save()
        return redirect('contactus')
    return render(request,'contactus.html')

def contactorg(request):
    arr=[]
    obj = contactOrg.objects.all()
    for i in obj:
        arr.append(i)
    params = {'params':arr}
    return render(request,'contactorg.html',params)
    
