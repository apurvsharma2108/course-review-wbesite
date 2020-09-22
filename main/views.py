from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def home(request):
    allCourses=Course.objects.all()
    context={
        'courses':allCourses,
    }

    return render(request,'main/index.html',context)
# details page
def detail(request,id):
    course=Course.objects.get(id=id)

    context={
        "course":course
    }
    return render(request,'main/details.html',context)
def add_courses(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form=CourseForm(request.POST or None)

                if form.is_valid():
                    data=form.save(commit=False)
                    data.save()
                    return redirect("main:home")
            else:
                form=CourseForm()
            return render(request,'main/addcourses.html',{"form":form,"controller":"Add Courses"})
        else:
            return redirect("main:home")
    return redirect("acounts:login")

def edit_courses(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            course=Course.objects.get(id=id)
            if request.method=="POST":
                form=CourseForm(request.POST or None,instance=course)

                if form.is_valid():
                    data=form.save(commit=False)
                    data.save()
                    return redirect("main:detail",id)
            else:
                form=CourseForm(instance=course)
            return render(request,'main/addcourses.html',{"form":form,"controller":"Edit Courses"})
        else:
            return redirect("main:home")
    return redirect("acounts:login")



def delete_courses(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            course=Course.objects.get(id=id)
            course.delete()
            return redirect("main:home")
        else:
            return redirect("main:home")
    return redirect("acounts:login")
