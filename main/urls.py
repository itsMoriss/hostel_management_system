from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('',views.index,name='index'),
    path('user-registration',views.user_registration,name='user_registration'),
    path('user-profile',views.user_profile,name='user_profile'),
    path('admin-dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin-details',views.admin_details,name='admin_details'),
    path('mess-details',views.mess_details,name='mess_details'),
    path('student-dashboard',views.student_dashboard,name='student_dashboard'),
    path('student-leave',views.student_leave,name='student_leave'),
    path('hostel-leave-details',views.hostel_leave_details,name='hostel_leave_details'),
    path('hostel-staff-details',views.hostel_staff_details,name='hostel_staff_details'),
    path('student-details',views.student_details,name='student_details'),
    path('delete-student/<pk>',views.delete_student,name='delete_student'),
    path('delete-menu/<pk>',views.delete_menu,name='delete_menu'),
    path('add-mess-menu',views.add_mess_menu,name='add_mess_menu'),
    path('edit-student/<pk>/',views.edit_student,name='edit_student'),
    path('edit-profile/<pk>/',views.edit_profile,name='edit_profile'),
    path('edit-hostel-staff/<pk>/',views.edit_hostel_staff,name='edit_hostel_staff'),
    path('add-student-leave/<pk>/',views.add_student_leave,name='add_student_leave'),
    path('all-students-leave/',views.all_students_leave,name='all_students_leave'),
    path('add-hostel',views.add_hostel,name='add_hostel'),
    path('add-fees',views.add_school_fees,name='add_school_fees'),
    path('fees-records',views.fees_records,name='fees_records'),
  
]

