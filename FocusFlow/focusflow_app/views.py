from django.shortcuts import render,redirect
from .models import Focus
from .forms import Focusform
from django.contrib.auth.decorators import login_required


# Create your views here.
def profile(request):
    return render (request,'focusflow_app/profile.html')

@login_required()
def create_focus(request):
    focuses=Focus.objects.all()
    if request.method == 'POST':
        form = Focusform(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=request.user
            data.save()
        return redirect ('create')    
    else:
        form = Focusform()
    return render (request,'focusflow_app/flow.html',{'form':form,'focuses':focuses})

def edit_focus(request, srno):
    obj = Focus.objects.get(srno=srno)
    if request.method == 'POST':
        form = Focusform(request.POST , instance=obj)
        if form.is_valid():
            form.save()
        return redirect ('create')    
    else:
        form = Focusform(instance = obj)
    return render(request,'focusflow_app/flow.html',{'form':form}) 

def delete_focus(request, srno):
    obj = Focus.objects.get(srno=srno)
    if request.method == 'POST':
        obj.delete()
        return redirect ('create')
    return render(request,'focusflow_app/flow.html',{'obj':obj})