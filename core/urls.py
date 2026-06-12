from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('register/', views.register, name='register'),

    path('login/', views.login, name='login'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

    path('apply-training/', views.apply_training, name='apply_training'),

    path('training-list/', views.training_list, name='training_list'),

    path('approve-training/<int:id>/', views.approve_training, name='approve_training'),

    path('reject-training/<int:id>/', views.reject_training, name='reject_training'),

    path('logout/', views.logout, name='logout'),

    path('add-attendance/', views.add_attendance, name='add_attendance'),

    path('attendance-list/', views.attendance_list, name='attendance_list'),

    path('upload-report/', views.upload_report, name='upload_report'),

    path('report-list/', views.report_list, name='report_list'),

    path('upload-certificate/', views.upload_certificate, name='upload_certificate'),

    path('certificate-list/', views.certificate_list, name='certificate_list'),

    path('delete-training/<int:id>/', views.delete_training, name='delete_training'),

    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('student-list/', views.student_list, name='student_list'),

    path(
    'admin-dashboard/',
    views.admin_dashboard,
    name='admin_dashboard'
)

]