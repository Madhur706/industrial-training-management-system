from django.shortcuts import render, redirect
from django.contrib import messages

from .models import (
    Register,
    Training,
    Attendance,
    Report,
    Certificate
)


# HOME PAGE

def index(request):

    return render(request, 'index.html')


# REGISTER

def register(request):

    if request.method == "POST":

        name = request.POST.get('name')

        email = request.POST.get('email')

        password = request.POST.get('password')

        confirm_password = request.POST.get('confirm_password')

        role = request.POST.get('role')

        # Password Match Check

        if password != confirm_password:

            messages.error(
                request,
                'Password and Confirm Password do not match'
            )

            return redirect('register')

        # Email Already Exists Check

        if Register.objects.filter(email=email).exists():

            messages.error(
                request,
                'Email already exists'
            )

            return redirect('register')

        # Save User

        Register.objects.create(
            name=name,
            email=email,
            password=password,
            role=role
        )

        messages.success(
            request,
            'Registration Successful'
        )

        return redirect('login')

    return render(request, 'register.html')

from django.contrib import messages


from django.contrib import messages


def login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = Register.objects.filter(
            email=email,
            password=password,
            role=role
        ).first()

        if user:

            request.session['user_id'] = user.id

            messages.success(
                request,
                "Successfully Login"
            )

            if user.role == "Admin":

                return redirect('/admin')

            elif user.role == "Trainer":

                return redirect('admin_dashboard')

            else:

                return redirect('student_dashboard')

        else:

            messages.error(
                request,
                "Wrong Email or Password"
            )

    return render(request, 'login.html')
# ADMIN DASHBOARD

def admin_dashboard(request):

    return render(request, 'admin_dashboard.html')



# STUDENT DASHBOARD

def student_dashboard(request):

    return render(request, 'student_dashboard.html')


# APPLY TRAINING

def apply_training(request):

    if request.method == "POST":

        student_name = request.POST.get('student_name')
        email = request.POST.get('email')
        company_name = request.POST.get('company_name')
        technology = request.POST.get('technology')
        duration = request.POST.get('duration')

        Training.objects.create(
            student_name=student_name,
            email=email,
            company_name=company_name,
            technology=technology,
            duration=duration
        )

    return render(request, 'apply_training.html')


# TRAINING LIST

def training_list(request):

    search = request.GET.get('search')

    if search:

        trainings = Training.objects.filter(
            student_name__icontains=search
        )

    else:

        trainings = Training.objects.all()

    return render(
        request,
        'training_list.html',
        {'trainings': trainings}
    )


# APPROVE TRAINING

def approve_training(request, id):

    training = Training.objects.get(id=id)

    training.status = "Approved"

    training.save()

    return redirect('training_list')


# REJECT TRAINING

def reject_training(request, id):

    training = Training.objects.get(id=id)

    training.status = "Rejected"

    training.save()

    return redirect('training_list')


# DELETE TRAINING

def delete_training(request, id):

    training = Training.objects.get(id=id)

    training.delete()

    return redirect('training_list')


# LOGOUT

def logout(request):

    return redirect('index')


# ADD ATTENDANCE

def add_attendance(request):

    students = Register.objects.filter(role="Student")

    if request.method == "POST":

        date = request.POST.get('date')

        for student in students:
            print("POST DATA =", request.POST)
            print("DATE =", date)
            status = request.POST.get(student.name)

            print(student.name, status)

            Attendance.objects.create(
                student_name=student.name,
                date=date,
                status=status
            )

        return redirect('admin_dashboard')

    return render(
        request,
        'admin_dashboard.html',
        {'students': students}
    )

def trainer_attendance(request):

    attendance = Attendance.objects.all()

    return render(
        request,
        'trainer_attendance.html',
        {'attendance': attendance}
    )

def attendance_list(request):

    user_id = request.session.get('user_id')

    if not user_id:

        return redirect('login')

    student = Register.objects.get(id=user_id)

    attendance = Attendance.objects.filter(
        student_name__iexact=student.name
    )

    return render(
        request,
        'attendance_list.html',
        {'attendance': attendance}
    )
def upload_report(request):

    if request.method == "POST":

        student_name = request.POST.get('student_name')

        report_file = request.FILES.get('report_file')

        Report.objects.create(
            student_name=student_name,
            report_file=report_file
        )

    return render(request, 'upload_report.html')


# REPORT LIST

def report_list(request):

    reports = Report.objects.all()

    return render(
        request,
        'report_list.html',
        {'reports': reports}
    )


# UPLOAD CERTIFICATE

def upload_certificate(request):

    if request.method == "POST":

        student_name = request.POST.get('student_name')

        certificate_file = request.FILES.get('certificate_file')

        Certificate.objects.create(
            student_name=student_name,
            certificate_file=certificate_file
        )

    return render(request, 'upload_certificate.html')


# CERTIFICATE LIST

def certificate_list(request):

    certificates = Certificate.objects.all()

    return render(
        request,
        'certificate_list.html',
        {'certificates': certificates}
    )


# PROFILE PAGE

def profile(request):

    user_id = request.session.get('user_id')

    if not user_id:

        return redirect('login')

    student = Register.objects.filter(id=user_id).first()

    if not student:

        return redirect('login')

    return render(
        request,
        'profile.html',
        {'student': student}
    )


# ABOUT PAGE

def about(request):

    return render(request, 'about.html')


# CONTACT PAGE

def contact(request):

    return render(request, 'contact.html')

def student_list(request):

    students = Register.objects.filter(role="Student")

    return render(
        request,
        'student_list.html',
        {'students': students}
    )