from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import  UpdateView,DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from Todoapp.forms import Todoform
from Todoapp.models import task


def home(request):
    model=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task' '')
        priority=request.POST.get('priority' '')
        date=request.POST.get('date' '')
        models=task(name=name,priority=priority,date=date)
        models.save()
    return render(request,"home.html",{'task':model})
# class tasklist(ListView):
#     model = task
#     template_name = "home.html"
#     context_object_name = "task"

# class taskdetail(DetailView):
#     model=task
#     template_name ='home.html'
#     context_object_name = "form"

class taskupdate(UpdateView):
    model=task
    template_name = "edit.html"
    fields = ('name','priority','date')
    success_url = reverse_lazy('home')

class taskdelete(DeleteView):
    model=task
    template_name = "delete.html"
    success_url = reverse_lazy('home')

# def delete(request,taskid):
#     Task=task.objects.get(id=taskid)
#     if request.method=='POST':
#         Task.delete()
#         return redirect("/")
#     return render(request, "delete.html")
#
# def update(request,id):
#     Task=task.objects.get(id=id)
#     form=Todoform(request.POST or None, instance=Task)
#     if form.is_valid():
#         form.save()
#         return redirect("/")
#     return render(request,"edit.html",{'form':form,'Task':Task})


