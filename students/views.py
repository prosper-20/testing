from django.shortcuts import render, redirect
from .models import Student
from django.core.exceptions import ValidationError
from .forms import StudentForm

def list_students(request):
    all_students = Student.objects.all()
    # return render(request, "students/all_students.html", {"all_students": all_students})
    return render(request, "students/new_template.html", {"all_students": all_students})


def retrieve_student(request, id_from_the_web):
    student = Student.objects.get(id=id_from_the_web)
    return render(request, "students/one_student.html", {"student": student})



def create_student(request):
    if request.method == "GET":
        form = StudentForm()
    else:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # save the form to the database
        return redirect("students/")
    return render(request, "students/create_student.html", {'form': form})






