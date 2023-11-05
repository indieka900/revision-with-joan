from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Student

def home(request):
    students = Student.objects.all().order_by('-age')
    context = {
        'students':students,
    }
    return render(request,'home.html', context)

def viewStudent(request,id):
    student = Student.objects.get(id = id)
    context = {
        'student':student,
    }
    return render(request,'viewStudent.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        reg_no = request.POST.get('reg_no')
        image = request.FILES['image']
        student = Student(name=name, age=age, profile=image, admission_number=reg_no)
        student.save()
        messages.success(request, f'Student {student.name} added successfully')
        return redirect ('/')
    return render(request,'add.html')

def update(request, id):
    #get the specific student to edit
    student = Student.objects.get(id=id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        reg_no = request.POST.get('reg_no')
        image = request.FILES['image']
    
        #asign the fields with the new data
        student.name = name
        student.age = age
        student.admission_number = reg_no
        student.profile = image
        
        if len(request.FILES) != 0:
            if len(student.profile) > 0:
                student.profile = request.FILES['image']
        
        #save the student with the new data
        student.save()
        messages.success(request, f'Student {student.name} updated successfully')
        return redirect('/')
    return render(request, 'update.html', {'student':student})

def searchStudent(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            students = Student.objects.filter(Q(name__icontains = query) | Q(age__icontains = query) | Q(admission_number__icontains = query))
            return render(request, 'search.html', {'students': students, 'query':query})

        return render(request, 'search.html')

def delete(request, id):
     student = Student.objects.get(id=id)
     student.delete()
     messages.success(request, f'Student {student.name} deleted successfully')
     return redirect('/')
     

# Create your views here.
#CRUD