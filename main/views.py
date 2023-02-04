from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Student
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q

# Create your views here.
def signIn(request):
    if request.method == 'GET':
        context = {'title':'iAcademy Log In'}
        return render(request, 'login.html', context)

    else:
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        
        else:
            messages.error(request, 'Incorrect username or password')

def signOut(request):
    logout(request)
    return redirect('login')


def register(request):
    context = {'title':'Register Admin'}
    if request.method == 'GET':
        context = {'title':'Register Admin'}
        return render(request, 'register.html', context)

    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            login(request, user)
            return redirect('dashboard')
        except:
            messages.error(request, 'Registration failed')
    
    return render(request, 'register.html', context)
    

def dashboard(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
 
    count = Student.objects.all().count()

    page_range = 10

    if request.GET.get('page_range'):
        page_range = request.GET.get('page_range')

    first_class_count = Student.objects.filter(cgpa='5').count()
    extra_year_count = Student.objects.filter(extra_year=True).count()
    students = Student.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(matric_no__icontains=search_query) | Q(department__icontains=search_query))
    paginator = Paginator(students, page_range)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_number = 1
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        page_obj = paginator.get_page(page_number)

    context = {'title':'Dashboard', 'students':students, 'page_obj':page_obj, 'paginator':paginator, 'count':count, 'first_class_count':first_class_count, 'extra_year_count':extra_year_count}
    return render(request, 'dashboard.html', context)

def registerStudent(request):
    if request.method == 'GET':
        context = {'title':'Register Student'}
        return render(request, 'registerStudent.html', context)

    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        department = request.POST['department']
        cgpa = request.POST['cgpa']
        level = request.POST['level']
        dob = request.POST['dob']
        matric_no = request.POST['matric_no']
        extra_year = request.POST['extra_year']
        student_image = request.FILES['student_image']

        try:
            student = Student.objects.create(first_name=first_name, last_name=last_name, age=age, department=department, cgpa=cgpa, level=level, dob=dob, matric_no=matric_no, extra_year=extra_year, student_image=student_image)
            student.save()

            return redirect('dashboard')
        
        except:
            messages.error(request, 'Student registration failed')

def editStudent(request, pk):
    if request.method == 'GET':
        student = Student.objects.get(id=pk)
        context = {'title':'Edit Student', 'student':student}
        return render(request, 'editStudent.html', context)

    else:
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        department = request.POST['department']
        cgpa = request.POST['cgpa']
        level = request.POST['level']
        dob = request.POST['dob']
        matric_no = request.POST['matric_no']
        extra_year = request.POST['extra_year']
        student_image = request.FILES['student_image']

        student = Student.objects.get(id=pk)

        student.first_name = first_name
        student.last_name = last_name
        student.age = age
        student.department = department
        student.cgpa = cgpa
        student.level = level
        student.dob = dob
        student.matric_no = matric_no
        student.extra_year = extra_year
        student.student_image = student_image

        student.save()

        return redirect('dashboard')


    

def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return redirect('dashboard')