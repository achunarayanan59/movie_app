from django.shortcuts import render
from . models import movie_list
# Create your views here.

def index(request):
    return render(request,'index.html')

def create(request):
    title=request.POST.get('title')
    year=request.POST.get('year')
    desc=request.POST.get('desc')
    if title and year and desc:
        movie_list_obj=movie_list(title=title,year=year,desc=desc)
        movie_list_obj.save()
    return render(request,'create.html')

def view(request):
    data_set=movie_list.objects.all()
    print(data_set)
    return render(request,'view.html',{'view_movies':data_set})

def edit(request,pk):
    edit_instance=movie_list.objects.get(pk=pk)
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        desc=request.POST.get('desc')
        
        if title and year and desc:
            edit_instance.title=title
            edit_instance.year=year
            edit_instance.desc=desc
            edit_instance.save()
    return render(request,'edit.html',{'movie_list':edit_instance})




def delete(request,pk):
    instance=movie_list.objects.get(pk=pk)
    instance.delete()
    movie_data=movie_list.objects.all()
    return render(request,'view.html',{'view_movies':movie_data})