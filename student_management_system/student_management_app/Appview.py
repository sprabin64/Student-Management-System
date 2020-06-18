import datetime
import re
import glob
import os
from student_management_app import handwriting_recognition
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from student_management_app.models import CustomUser, Courses, Subjects, Staffs, Students


def admin_homepage(request):
    if request.method=="POST":
        uploaded_file =request.FILES['document']
        fs=FileSystemStorage()
        name = uploaded_file.name
        name = "1.png"
        files = glob.glob('C:/Users/USER/Google Drive/Desktop/FYP/test program django/student-management-system/student_management_system/media/*')
        for f in files:
            os.remove(f)
        fs.save(name,uploaded_file)
        handwriting_recognition.finalProgram()
        return HttpResponseRedirect("/add_student_form")

    else:
        return render(request, "main_pages/home_content.html")

def staff_homepage(request):
    if request.method=="POST":
        uploaded_file =request.FILES['document']
        fs=FileSystemStorage()
        name = uploaded_file.name
        name = "1.png"
        files = glob.glob('C:/Users/USER/Google Drive/Desktop/FYP/test program django/student-management-system/student_management_system/media/*')
        for f in files:
            os.remove(f)
        fs.save(name,uploaded_file)
        handwriting_recognition.finalProgram()
        return HttpResponseRedirect("/add_student_form")

    else:
        return render(request, "main_pages/staff_content.html")

def student_homepage(request):
    students = Students.objects.all()
    return render(request, "main_pages/student_content.html", {"students": students})

def add_staff(request):
    return render(request, "main_pages/add_staff.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type = 2)
            user.staffs.address=address
            user.save()
            messages.success(request, "Added Staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request, "Failed to add staff")
            return HttpResponseRedirect("/add_staff")


def add_course(request):
    return render(request, "main_pages/add_course.html")


def add_course_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("Method not allowed")
    else:
        course= request.POST.get("course")
        try:
            course_model = Courses(course_name= course)
            course_model.save()
            messages.success(request, "Added Course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Failed to add course")
            return HttpResponseRedirect("/add_course")

def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    if request.method=="POST":
        course.delete()
    return HttpResponseRedirect("/manage_course")


def add_student(request):
    courses = Courses.objects.all()
    return render(request, "main_pages/add_student.html", {"courses":courses})

def add_student_form(request):
    courses = Courses.objects.all()


    with open('C:/Users/USER/Google Drive/Desktop/FYP/Program/extract.txt') as file:
        fin = file.read()
        try:
            # Test = re.search('First Name(.*?)Last Name', fin).group(1)
            First_Name = re.search('First Name(.*?)Last Name', fin).group(1)
            Last_name = re.search('Last Name(.*?)Gender', fin).group(1)
            Gender = re.search('Gender(.*?)Address', fin).group(1)
            Address = re.search('Address(.*?)Email', fin).group(1)
            Email = re.search('Email(.*?)End', fin).group(1)
        except:
            print("Match not found")

        '''print(Name)
        print(Address)
        print(Phone_Number)
        print(Email)'''

        file.close()
        f = open('C:/Users/USER/Google Drive/Desktop/FYP/Program/extract.txt', 'w')
        # f.write(" ")
        f.close()
        print("test")
    fname = First_Name
    lname = Last_name
    address = Address
    gender = Gender
    email = Email

    return render(request, "main_pages/testadd.html",
                  {"courses": courses, "fname": fname, "lname": lname, "address": address, "gender": gender,
                   "email": email})

def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = "2020-06-08"#request.POST.get("session_start")
        session_end = "2023-06-08"#request.POST.get("session_end")
        course_id = request.POST.get("course")
        sex = request.POST.get("sex")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=3)
            user.students.address = address
            course_obj= Courses.objects.get(id = course_id)
            user.students.course_id = course_obj
            user.students.session_start_year= session_start
            user.students.session_end_year= session_end
            user.students.gender= sex
            user.students.profile_pic=""
            user.save()
            messages.success(request, "Added Student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to add student")
            return HttpResponseRedirect("/add_student")

def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, "main_pages/add_subject.html", {"courses":courses, "staffs":staffs })

def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        subject_name =request.POST.get("subject")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)
        try:
            subject = Subjects(subject_name= subject_name, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request, "Added Subject")
            return HttpResponseRedirect("/add_subject")
        except:
            messages.error(request, "Failed to add subject")
            return HttpResponseRedirect("/add_subject")

def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(request,"main_pages/manage_staff.html", {"staffs":staffs})

def manage_student(request):
    students = Students.objects.all()
    return render(request,"main_pages/manage_student.html", {"students":students})


def manage_course(request):
    courses = Courses.objects.all()
    return render(request, "main_pages/manage_course.html", {"courses":courses})

def manage_subject(request):
    subjects = Subjects.objects.all()
    return render(request, "main_pages/manage_subject.html", {"subjects":subjects})

def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request, "main_pages/edit_staff.html", {"staff":staff})

def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")
        try:

            user = CustomUser.objects.get(id = staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.first_name = first_name
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()

            messages.success(request, "Edited Staff details")
            return HttpResponseRedirect("/edit_staff/"+staff_id)
        except:
            messages.error(request, "Failed to edit staff details")
            return HttpResponseRedirect("/edit_staff/"+staff_id)

def edit_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    courses = Courses.objects.all()
    return render(request, "main_pages/edit_student.html", {"student":student, "courses":courses})

def delete_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    user = CustomUser.objects.get(id=student_id)
    if request.method=="POST":
        student.delete()
        user.delete()
    return HttpResponseRedirect("/manage_student")


def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not allowed</h2>")

    else:
        student_id =request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        session_start = "2020-06-08"#request.POST.get("session_start")
        session_end = "2023-06-08"#request.POST.get("session_end")
        course_id = request.POST.get("course")
        sex = request.POST.get("sex")

        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name= first_name
            user.last_name= last_name
            user.username= username
            user.email= email
            user.save()

            student = Students.objects.get(admin=student_id)
            student.address = address
            student.session_start_year = session_start
            student.session_end_year = session_end
            student.gender = sex
            course = Courses.objects.get(id=course_id)
            student.course_id= course
            student.save()
            messages.success(request, "edited Student details")
            return HttpResponseRedirect("/edit_student/"+student_id)
        except:
            messages.error(request, "Failed to edit student details")
            return HttpResponseRedirect("/edit_student/"+student_id)





