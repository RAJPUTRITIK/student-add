

from django.shortcuts import render,HttpResponseRedirect

from .form import studentregistration
from .models import user

# Create your views here.


#this funtion will add new item and show all items
def add_show(request):
    if request.method=='POST':
        fm=studentregistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=user(name=nm, email=em, password=pw)
            reg.save()
            fm=studentregistration()

    else:
        fm=studentregistration()
    stud=user.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu':stud}) 

#tthis funtion will update/edit
def update_data(request,id):
    if request.method == 'POST':
        pi=user.objects.get(pk=id)
        fm=studentregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=user.objects.get(pk=id)
        fm=studentregistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})



    # this funtion will delete
def delete_items(request,id):
    pi = user.objects.get(pk=id)
    if request.method == 'POST':
        pi.delete()
        return HttpResponseRedirect('/')

    