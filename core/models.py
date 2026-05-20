from django.db import models


class Register(models.Model):

    
    ROLE_CHOICES = (

    ('Student', 'Student'),
    ('Trainer', 'Trainer'),
    ('Admin', 'Admin'),

)

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


class Training(models.Model):

    STATUS_CHOICES = (

        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),

    )

    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=200)
    technology = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return self.student_name


class Attendance(models.Model):

    student_name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name


class Report(models.Model):

    student_name = models.CharField(max_length=100)

    report_file = models.FileField(
        upload_to='reports/'
    )

    def __str__(self):
        return self.student_name


class Certificate(models.Model):

    student_name = models.CharField(max_length=100)

    certificate_file = models.FileField(
        upload_to='certificates/'
    )

    def __str__(self):
        return self.student_name